"""Per-request ComPDF credentials kept out of tool arguments and logs."""

from __future__ import annotations

import contextvars

from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send


_api_key: contextvars.ContextVar[str | None] = contextvars.ContextVar("compdf_api_key", default=None)


def request_api_key() -> str:
    api_key = _api_key.get()
    if not api_key:
        raise ValueError("X-ComPDF-API-Key is required for MCP requests.")
    return api_key


class ComPDFCredentialMiddleware:
    """Require each MCP POST request to carry its user's ComPDF API Key."""

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or scope.get("method") != "POST" or not scope.get("path", "").startswith("/mcp"):
            await self.app(scope, receive, send)
            return
        headers = {name.decode("latin-1").lower(): value.decode("latin-1") for name, value in scope.get("headers", [])}
        api_key = headers.get("x-compdf-api-key", "").strip()
        if not api_key:
            await JSONResponse({"error": "compdf_api_key_required"}, status_code=401)(scope, receive, send)
            return
        token = _api_key.set(api_key)
        try:
            await self.app(scope, receive, send)
        finally:
            _api_key.reset(token)
