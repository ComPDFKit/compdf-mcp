"""Small dependency-free operational middleware for the HTTP service."""

from __future__ import annotations

import logging
import os
import time
import uuid
from hashlib import sha256
from collections import defaultdict, deque

from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp, Receive, Scope, Send


logger = logging.getLogger("compdf_streaming_mcp.audit")
REQUEST_COUNTS: dict[tuple[str, int], int] = defaultdict(int)


class RequestAuditMiddleware:
    """Emit request metadata only; never log bodies, credentials, or file names."""

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        started = time.monotonic()
        request_id = uuid.uuid4().hex
        status_code = 500

        async def audited_send(message):
            nonlocal status_code
            if message["type"] == "http.response.start":
                status_code = message["status"]
                headers = list(message.get("headers", []))
                headers.append((b"x-request-id", request_id.encode("ascii")))
                message = {**message, "headers": headers}
            await send(message)

        try:
            await self.app(scope, receive, audited_send)
        finally:
            logger.info(
                "request_complete request_id=%s method=%s path=%s status=%s duration_ms=%d",
                request_id,
                scope.get("method"),
                scope.get("path"),
                status_code,
                (time.monotonic() - started) * 1000,
            )
            REQUEST_COUNTS[(scope.get("path", "unknown"), status_code)] += 1


class RateLimitMiddleware:
    """In-memory defensive rate limiter; use an external shared limiter at scale."""

    def __init__(self, app: ASGIApp) -> None:
        self.app = app
        self.limit = int(os.getenv("MCP_RATE_LIMIT_PER_MINUTE", "120"))
        self.windows: dict[str, deque[float]] = defaultdict(deque)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or self.limit <= 0:
            await self.app(scope, receive, send)
            return
        request = Request(scope)
        client = request.client.host if request.client else "unknown"
        authorization = request.headers.get("authorization", "")
        # Do not retain raw bearer credentials in the rate-limit map.
        identity = sha256(authorization.encode("utf-8")).hexdigest() if authorization else client
        now = time.monotonic()
        window = self.windows[identity]
        while window and window[0] <= now - 60:
            window.popleft()
        if len(window) >= self.limit:
            await JSONResponse({"error": "rate_limited"}, status_code=429, headers={"Retry-After": "60"})(scope, receive, send)
            return
        window.append(now)
        await self.app(scope, receive, send)
