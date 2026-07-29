"""ComPDF v2 gateway used by the Streaming HTTP MCP applications."""

from __future__ import annotations

import base64
import binascii
import json
import mimetypes
import os
import uuid
from dataclasses import dataclass
from typing import Any, Mapping, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .catalog import Operation, get_operation
from .credentials import request_api_key


GLOBAL_API_BASE_URL = "https://api-server.compdf.com/server"
MAX_FILE_BYTES = 100 * 1024 * 1024
SPECIAL_FILE_FIELDS = {"htmlFile", "templateFile", "dataFile", "imageFile", "iccFile"}
SENSITIVE_FIELDS = {"password", "userPassword", "ownerPassword", "fileParameter"}


class ComPDFGatewayError(RuntimeError):
    """A validation, transport, or provider error from the ComPDF API."""


@dataclass(frozen=True)
class UploadedFile:
    filename: str
    content: bytes
    content_type: str


class ComPDFGateway:
    """Calls only catalogued ComPDF v2 API paths using multipart requests."""

    def __init__(self, api_key: str, base_url: str = GLOBAL_API_BASE_URL, timeout_seconds: float = 180) -> None:
        if not api_key:
            raise ValueError("A ComPDF API key is required.")
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout_seconds = timeout_seconds

    @classmethod
    def from_request(cls) -> "ComPDFGateway":
        return cls(
            api_key=request_api_key(),
            base_url=os.getenv("COMPDF_API_BASE_URL", GLOBAL_API_BASE_URL),
            timeout_seconds=float(os.getenv("COMPDF_API_TIMEOUT_SECONDS", "180")),
        )

    def invoke_sync(
        self,
        operation_name: str,
        files: Sequence[Mapping[str, str]] = (),
        options: Mapping[str, Any] | None = None,
        special_files: Mapping[str, Mapping[str, str]] | None = None,
    ) -> Any:
        operation, uploads, fields = self._prepare(operation_name, files, options, special_files)
        return self._post(operation.path, uploads, fields)

    def invoke_async(
        self,
        operation_name: str,
        files: Sequence[Mapping[str, str]] = (),
        options: Mapping[str, Any] | None = None,
        special_files: Mapping[str, Mapping[str, str]] | None = None,
    ) -> Any:
        operation, uploads, fields = self._prepare(operation_name, files, options, special_files)
        return self._post(operation.path.replace("/v2/process/", "/v2/processAsync/", 1), uploads, fields)

    def create_presigned(
        self,
        operation_name: str,
        file: Mapping[str, str],
        options: Mapping[str, Any] | None = None,
    ) -> tuple[dict[str, Any], UploadedFile]:
        operation = get_operation(operation_name)
        if operation.min_files != 1 or operation.max_files != 1:
            raise ValueError("Presigned mode currently supports one-standard-file operations only; use async mode for this operation.")
        upload = decode_file(file)
        fields = normalise_options(options)
        fields["fileName"] = upload.filename
        data = self._post(operation.path.replace("/v2/process/", "/v2/presignedUrl/", 1), [], fields)
        if not isinstance(data, dict) or not data.get("taskId") or not data.get("presignedUrl"):
            raise ComPDFGatewayError("ComPDF presigned response did not include taskId and presignedUrl.")
        return data, upload

    def upload_presigned(self, url: str, file: UploadedFile) -> None:
        request = Request(url, data=file.content, method="PUT", headers={"Content-Type": file.content_type})
        try:
            with urlopen(request, timeout=self._timeout_seconds):
                return
        except HTTPError as error:
            raise ComPDFGatewayError(f"Presigned upload HTTP {error.code}: {error.read().decode('utf-8', 'replace')}") from error
        except URLError as error:
            raise ComPDFGatewayError(f"Presigned upload failed: {error.reason}") from error

    def start_presigned(self, task_id: str, language: int = 1) -> Any:
        return self._get("/v2/execute/start", {"taskId": task_id, "language": language})

    def task_status(self, task_id: str, language: int = 1) -> Any:
        return self._get("/v2/task/taskInfo", {"taskId": task_id, "language": language})

    def _prepare(
        self,
        operation_name: str,
        files: Sequence[Mapping[str, str]],
        options: Mapping[str, Any] | None,
        special_files: Mapping[str, Mapping[str, str]] | None,
    ) -> tuple[Operation, list[tuple[str, UploadedFile]], dict[str, str]]:
        operation = get_operation(operation_name)
        standard_files = [decode_file(file) for file in files]
        if len(standard_files) < operation.min_files:
            raise ValueError(f"{operation_name} requires at least {operation.min_files} file(s).")
        if operation.max_files is not None and len(standard_files) > operation.max_files:
            raise ValueError(f"{operation_name} accepts at most {operation.max_files} file(s).")
        fields = normalise_options(options)
        if operation_name == "document_extract" and "extractFields" not in fields:
            raise ValueError("document_extract requires options.extractFields.")
        if operation_name == "generate_pdf" and not any(key in fields for key in ("html", "htmlUrl", "template")) and not special_files:
            raise ValueError("generate_pdf requires html, htmlUrl, template, or an HTML/template file.")

        uploads: list[tuple[str, UploadedFile]] = [("file", file) for file in standard_files]
        for field, raw_file in (special_files or {}).items():
            if field not in SPECIAL_FILE_FIELDS:
                raise ValueError(f"Unsupported special file field: {field}")
            uploads.append((field, decode_file(raw_file)))
        return operation, uploads, fields

    def _post(self, path: str, files: Sequence[tuple[str, UploadedFile]], fields: Mapping[str, str]) -> Any:
        content_type, body = multipart_body(files, fields)
        request = Request(
            f"{self._base_url}{path}",
            data=body,
            method="POST",
            headers={"x-api-key": self._api_key, "Content-Type": content_type, "Accept": "application/json"},
        )
        return self._request_json(request)

    def _get(self, path: str, query: Mapping[str, Any]) -> Any:
        request = Request(
            f"{self._base_url}{path}?{urlencode(query)}",
            method="GET",
            headers={"x-api-key": self._api_key, "Accept": "application/json"},
        )
        return self._request_json(request)

    def _request_json(self, request: Request) -> Any:
        try:
            with urlopen(request, timeout=self._timeout_seconds) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            raise ComPDFGatewayError(f"ComPDF HTTP {error.code}: {error.read().decode('utf-8', 'replace')}") from error
        except URLError as error:
            raise ComPDFGatewayError(f"Could not reach ComPDF API: {error.reason}") from error
        except json.JSONDecodeError as error:
            raise ComPDFGatewayError("ComPDF returned a non-JSON response.") from error
        if str(payload.get("code")) != "200":
            raise ComPDFGatewayError(f"ComPDF error {payload.get('code')}: {payload.get('msg', 'Unknown error')}")
        return strip_sensitive(payload.get("data"))


def decode_file(raw: Mapping[str, str]) -> UploadedFile:
    filename = raw.get("filename", "").strip()
    encoded = raw.get("content_base64", "")
    if not filename or not encoded:
        raise ValueError("Each file requires filename and content_base64.")
    if "/" in filename or "\\" in filename:
        raise ValueError("filename must not contain a path.")
    try:
        content = base64.b64decode(encoded, validate=True)
    except (ValueError, binascii.Error) as error:
        raise ValueError(f"{filename} has invalid content_base64.") from error
    if len(content) > MAX_FILE_BYTES:
        raise ValueError(f"{filename} exceeds the 100 MB streaming upload limit.")
    return UploadedFile(filename, content, raw.get("content_type") or mimetypes.guess_type(filename)[0] or "application/octet-stream")


def normalise_options(options: Mapping[str, Any] | None) -> dict[str, str]:
    fields: dict[str, str] = {}
    for name, value in (options or {}).items():
        if name == "file" or name in SPECIAL_FILE_FIELDS:
            raise ValueError(f"Upload '{name}' through files or special_files, not options.")
        if value is None:
            continue
        if isinstance(value, bool):
            fields[name] = "true" if value else "false"
        elif isinstance(value, (str, int, float)):
            fields[name] = str(value)
        elif isinstance(value, (list, dict)):
            fields[name] = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        else:
            raise ValueError(f"Unsupported value for option '{name}'.")
    return fields


def multipart_body(files: Sequence[tuple[str, UploadedFile]], fields: Mapping[str, str]) -> tuple[str, bytes]:
    boundary = f"----ComPDFStreamingMCP{uuid.uuid4().hex}"
    separator = f"--{boundary}\r\n".encode("ascii")
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.extend((separator, f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(), value.encode(), b"\r\n"))
    for field, file in files:
        chunks.extend((
            separator,
            f'Content-Disposition: form-data; name="{field}"; filename="{file.filename}"\r\n'.encode(),
            f"Content-Type: {file.content_type}\r\n\r\n".encode(),
            file.content,
            b"\r\n",
        ))
    chunks.append(f"--{boundary}--\r\n".encode("ascii"))
    return f"multipart/form-data; boundary={boundary}", b"".join(chunks)


def strip_sensitive(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: strip_sensitive(item) for key, item in value.items() if key not in SENSITIVE_FIELDS}
    if isinstance(value, list):
        return [strip_sensitive(item) for item in value]
    return value
