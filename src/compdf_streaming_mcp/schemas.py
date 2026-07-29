"""Reviewed ComPDF OpenAPI parameter schemas and MCP input validation."""

from __future__ import annotations

import json
from importlib.resources import files
from typing import Any, Mapping

from .catalog import Operation


_RAW_SCHEMAS = json.loads(
    files("compdf_streaming_mcp").joinpath("official_parameter_schemas.json").read_text(encoding="utf-8")
)["operations"]
SPECIAL_FILE_FIELDS = frozenset({"htmlFile", "templateFile", "dataFile", "imageFile", "iccFile"})

FILE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "description": "A file encoded for MCP transport; content never appears in logs.",
    "properties": {
        "filename": {"type": "string", "minLength": 1},
        "content_base64": {"type": "string", "minLength": 1, "contentEncoding": "base64"},
        "content_type": {"type": "string"},
    },
    "required": ["filename", "content_base64"],
    "additionalProperties": False,
}


def operation_parameters(operation_name: str) -> dict[str, Any]:
    """Return the generated official request parameters for one operation."""

    try:
        return _RAW_SCHEMAS[operation_name]
    except KeyError as error:  # pragma: no cover - protected by catalogue tests
        raise ValueError(f"No official parameter schema for operation '{operation_name}'.") from error


def operation_input_schema(operation: Operation) -> dict[str, Any]:
    """Create the public MCP schema while retaining multipart file semantics."""

    spec = operation_parameters(operation.name)
    option_properties: dict[str, Any] = {}
    special_properties: dict[str, Any] = {}
    for name, definition in spec["properties"].items():
        if name == "file":
            continue
        if name in SPECIAL_FILE_FIELDS:
            special_properties[name] = {
                **FILE_SCHEMA,
                "description": f"{definition.get('description', name)} Supply this official binary field as an MCP file object.",
            }
        else:
            option_properties[name] = definition

    required_options = [_canonical_parameter_name(name, option_properties) for name in spec.get("required", [])]
    required_options = [name for name in required_options if name in option_properties]
    schema: dict[str, Any] = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "files": {
                "type": "array",
                "description": f"Standard input files ({operation.min_files} to "
                + ("unlimited" if operation.max_files is None else str(operation.max_files))
                + ").",
                "items": FILE_SCHEMA,
                "minItems": operation.min_files,
                **({"maxItems": operation.max_files} if operation.max_files is not None else {}),
            },
            "options": {
                "type": "object",
                "description": "Official ComPDF multipart parameters for this operation. Unknown fields are rejected.",
                "properties": option_properties,
                "required": required_options,
                "additionalProperties": False,
            },
            "special_files": {
                "type": "object",
                "description": "Official binary multipart parameters, encoded as MCP file objects.",
                "properties": special_properties,
                "additionalProperties": False,
            },
        },
        "required": ["files"] if operation.min_files else [],
    }
    return schema


def validate_operation_input(
    operation: Operation,
    files: list[Mapping[str, Any]],
    options: Mapping[str, Any] | None,
    special_files: Mapping[str, Mapping[str, Any]] | None,
) -> None:
    """Enforce the reviewed OpenAPI schema before creating a provider request."""

    spec = operation_parameters(operation.name)
    properties: Mapping[str, Mapping[str, Any]] = spec["properties"]
    supplied_options = options or {}
    supplied_special_files = special_files or {}

    unknown = set(supplied_options) - set(properties) - {"file"}
    if unknown:
        raise ValueError(f"Unsupported {operation.name} option(s): {', '.join(sorted(unknown))}.")
    misplaced = set(supplied_options) & SPECIAL_FILE_FIELDS
    if misplaced:
        raise ValueError(f"Upload {', '.join(sorted(misplaced))} through special_files, not options.")
    unknown_special = set(supplied_special_files) - SPECIAL_FILE_FIELDS
    if unknown_special:
        raise ValueError(f"Unsupported special file field(s): {', '.join(sorted(unknown_special))}.")
    not_supported_special = set(supplied_special_files) - set(properties)
    if not_supported_special:
        raise ValueError(f"{operation.name} does not support special file field(s): {', '.join(sorted(not_supported_special))}.")

    for required in spec.get("required", []):
        name = _canonical_parameter_name(required, properties)
        if name == "file":
            continue
        if name in SPECIAL_FILE_FIELDS:
            if name not in supplied_special_files:
                raise ValueError(f"{operation.name} requires special_files.{name}.")
        elif name not in supplied_options:
            raise ValueError(f"{operation.name} requires options.{name}.")

    for name, value in supplied_options.items():
        _validate_value(operation.name, name, value, properties[name])


def _canonical_parameter_name(name: str, properties: Mapping[str, Any]) -> str:
    """Resolve a known documentation typo such as extract_fields/extractFields."""

    if name in properties:
        return name
    parts = name.split("_")
    camel = parts[0] + "".join(part.title() for part in parts[1:])
    return camel if camel in properties else name


def _validate_value(operation: str, name: str, value: Any, definition: Mapping[str, Any]) -> None:
    expected = definition.get("type")
    valid = (
        expected is None
        or (expected == "string" and isinstance(value, str))
        or (expected == "integer" and isinstance(value, int) and not isinstance(value, bool))
        or (expected == "number" and isinstance(value, (int, float)) and not isinstance(value, bool))
        or (expected == "boolean" and isinstance(value, bool))
        or (expected == "array" and isinstance(value, list))
        or (expected == "object" and isinstance(value, Mapping))
    )
    if not valid:
        raise ValueError(f"{operation}.{name} must be a {expected} according to the ComPDF OpenAPI schema.")
    enum = definition.get("enum")
    if enum is not None and value not in enum:
        raise ValueError(f"{operation}.{name} must be one of: {', '.join(map(str, enum))}.")
