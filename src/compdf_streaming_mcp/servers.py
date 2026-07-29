"""Module-scoped Streaming HTTP MCP applications."""

from __future__ import annotations

import os
from typing import Any, Mapping

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from .auth import configured_auth
from .catalog import MODULES, OPERATIONS, Operation, get_operation, operations_for
from .gateway import ComPDFGateway, ComPDFGatewayError
from .schemas import operation_input_schema, validate_operation_input


def build_module_server(module: str) -> FastMCP:
    """Create a module server, or the all-operation server when module is ``all``."""

    aggregate = module == "all"
    operations = list(OPERATIONS.values()) if aggregate else operations_for(module)
    label = "All APIs" if aggregate else f"{module.title()} API"
    # The MCP transport compares the complete HTTP Host header.  A normal
    # local request therefore arrives as ``127.0.0.1:8000`` rather than just
    # ``127.0.0.1``.  Keep the bare forms for tests/default-port deployments
    # and accept any local port for the development defaults.
    allowed_hosts = [
        host.strip()
        for host in os.getenv(
            "MCP_ALLOWED_HOSTS",
            "localhost,localhost:*,127.0.0.1,127.0.0.1:*,[::1],[::1]:*,testserver",
        ).split(",")
        if host.strip()
    ]
    allowed_origins = [origin.strip() for origin in os.getenv("MCP_ALLOWED_ORIGINS", "").split(",") if origin.strip()]
    auth, token_verifier = configured_auth()
    server = FastMCP(
        name=f"ComPDF {label}",
        instructions=(
            f"This is the ComPDF API v2 {label.lower()} endpoint. Invoke only the tools exposed "
            "by this endpoint. Files are objects with filename, content_base64, and optional content_type. "
            "ComPDF-specific parameters are sent in options using their exact official camelCase names."
        ),
        streamable_http_path="/mcp",
        stateless_http=False,
        auth=auth,
        token_verifier=token_verifier,
        transport_security=TransportSecuritySettings(allowed_hosts=allowed_hosts, allowed_origins=allowed_origins),
    )
    presigned_jobs: dict[str, tuple[str, str]] = {}

    for operation in operations:
        _register_sync_tool(server, operation)

    @server.tool(name="list_operations", description="List every ComPDF API v2 operation served by this route prefix.")
    def list_module_operations() -> list[dict[str, Any]]:
        return [_operation_summary(operation) for operation in operations]

    @server.tool(name="start_async_operation", description="Start a ComPDF /v2/processAsync task for an operation in this module.")
    def start_async_operation(
        operation: str,
        files: list[dict[str, str]] | None = None,
        options: dict[str, Any] | None = None,
        special_files: dict[str, dict[str, str]] | None = None,
    ) -> dict[str, Any]:
        try:
            selected = _module_operation(module, operation)
            result = ComPDFGateway.from_request().invoke_async(operation, files or [], options, special_files)
            return {
                "success": True,
                "operation": selected.name,
                "documentation_url": selected.documentation_url,
                "task_id": result.get("taskId") if isinstance(result, dict) else None,
                "result": result,
            }
        except (ValueError, ComPDFGatewayError) as error:
            return _error(operation, error)

    @server.tool(name="create_presigned_upload", description="Create a single-file ComPDF presigned upload task in this module.")
    def create_presigned_upload(
        operation: str,
        file: dict[str, str],
        options: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        try:
            selected = _module_operation(module, operation)
            result, upload = ComPDFGateway.from_request().create_presigned(operation, file, options)
            task_id = str(result["taskId"])
            presigned_jobs[task_id] = (str(result["presignedUrl"]), upload.filename)
            return {
                "success": True,
                "operation": selected.name,
                "documentation_url": selected.documentation_url,
                "task_id": task_id,
                "expected_file_name": upload.filename,
                "next_step": "Call upload_presigned_file with the same task_id and the same file name.",
            }
        except (ValueError, ComPDFGatewayError) as error:
            return _error(operation, error)

    @server.tool(name="upload_presigned_file", description="Upload a base64 file to the ComPDF presigned task created by this module.")
    def upload_presigned_file(task_id: str, file: dict[str, str]) -> dict[str, Any]:
        job = presigned_jobs.get(task_id)
        if not job:
            return {"success": False, "task_id": task_id, "error": "Unknown presigned task in this module server."}
        url, expected_name = job
        try:
            from .gateway import decode_file

            upload = decode_file(file)
            if upload.filename != expected_name:
                raise ValueError(f"Expected file name '{expected_name}'.")
            ComPDFGateway.from_request().upload_presigned(url, upload)
            return {"success": True, "task_id": task_id, "next_step": "Call start_presigned_operation."}
        except (ValueError, ComPDFGatewayError) as error:
            return {"success": False, "task_id": task_id, "error": str(error)}

    @server.tool(name="start_presigned_operation", description="Start an uploaded ComPDF presigned task in this module.")
    def start_presigned_operation(task_id: str, language: int = 1) -> dict[str, Any]:
        if task_id not in presigned_jobs:
            return {"success": False, "task_id": task_id, "error": "Unknown presigned task in this module server."}
        try:
            result = ComPDFGateway.from_request().start_presigned(task_id, language)
            presigned_jobs.pop(task_id, None)
            return {"success": True, "task_id": task_id, "result": result}
        except (ValueError, ComPDFGatewayError) as error:
            return {"success": False, "task_id": task_id, "error": str(error)}

    @server.tool(name="get_task_status", description="Query the documented ComPDF /v2/task/taskInfo endpoint.")
    def get_task_status(task_id: str, language: int = 1) -> dict[str, Any]:
        try:
            return {"success": True, "task_id": task_id, "result": ComPDFGateway.from_request().task_status(task_id, language)}
        except (ValueError, ComPDFGatewayError) as error:
            return {"success": False, "task_id": task_id, "error": str(error)}

    return server


def _register_sync_tool(server: FastMCP, operation: Operation) -> None:
    def invoke(
        files: list[dict[str, str]] | None = None,
        options: dict[str, Any] | None = None,
        special_files: dict[str, dict[str, str]] | None = None,
    ) -> dict[str, Any]:
        """Proxy one documented ComPDF synchronous operation."""

        try:
            validate_operation_input(operation, files or [], options, special_files)
            result = ComPDFGateway.from_request().invoke_sync(operation.name, files or [], options, special_files)
            return {
                "success": True,
                "operation": operation.name,
                "documentation_url": operation.documentation_url,
                "result": result,
                "download_url_expires_in_hours": 24,
            }
        except (ValueError, ComPDFGatewayError) as error:
            return _error(operation.name, error)

    invoke.__name__ = operation.name
    invoke.__doc__ = (
        f"{operation.description} ComPDF endpoint: {operation.path}. "
        f"See {operation.documentation_url} for exact options."
    )
    server.tool(name=operation.name, description=invoke.__doc__)(invoke)
    tool = server._tool_manager.get_tool(operation.name)
    if tool is None:  # pragma: no cover - FastMCP always registers the decorator result
        raise RuntimeError(f"Failed to register tool '{operation.name}'.")
    tool.parameters = operation_input_schema(operation)


def _module_operation(module: str, name: str) -> Operation:
    operation = get_operation(name)
    if module != "all" and operation.module != module:
        raise ValueError(f"Operation '{name}' belongs to the {operation.module} MCP route, not {module}.")
    return operation


def _operation_summary(operation: Operation) -> dict[str, Any]:
    return {
        "name": operation.name,
        "upstream_path": operation.path,
        "description": operation.description,
        "documentation_url": operation.documentation_url,
        "min_files": operation.min_files,
        "max_files": operation.max_files,
    }


def _error(operation: str, error: Exception) -> dict[str, Any]:
    return {"success": False, "operation": operation, "error": str(error)}
