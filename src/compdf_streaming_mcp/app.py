"""ASGI application mounting ComPDF Streaming HTTP MCP module endpoints."""

from __future__ import annotations

import os
from contextlib import AsyncExitStack, asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Mount, Route

from .servers import build_module_server
from .observability import REQUEST_COUNTS, RateLimitMiddleware, RequestAuditMiddleware
from .credentials import ComPDFCredentialMiddleware


load_dotenv()

async def healthz(_request):
    return JSONResponse(
        {
            "status": "ok",
            "protocol": "MCP Streamable HTTP",
            "routes": [
                "/mcp",
                "/mcp/conversion/mcp",
                "/mcp/ai/mcp",
                "/mcp/pdf/mcp",
                "/mcp/generate/mcp",
            ],
        }
    )


async def readyz(_request):
    """Readiness is configuration-only; upstream API calls stay out of probes."""

    return JSONResponse({"status": "ready"})


async def metrics(_request):
    lines = ["# TYPE compdf_mcp_http_requests_total counter"]
    for (path, status), count in sorted(REQUEST_COUNTS.items()):
        lines.append(f'compdf_mcp_http_requests_total{{path="{path}",status="{status}"}} {count}')
    return PlainTextResponse("\n".join(lines) + "\n", media_type="text/plain; version=0.0.4")


def create_app() -> Starlette:
    """Build a fresh ASGI app with a market-ready aggregate endpoint and module routes."""

    aggregate_server = build_module_server("all")
    conversion_server = build_module_server("conversion")
    ai_server = build_module_server("ai")
    pdf_server = build_module_server("pdf")
    generate_server = build_module_server("generate")

    @asynccontextmanager
    async def lifespan(_app):
        # Mounted Starlette applications do not automatically enter their child
        # lifespans. Each FastMCP streamable session manager must run for initialize,
        # session resumption, and SSE streaming to work on its route prefix.
        async with AsyncExitStack() as stack:
            for server in (aggregate_server, conversion_server, ai_server, pdf_server, generate_server):
                await stack.enter_async_context(server.session_manager.run())
            yield

    return Starlette(
        lifespan=lifespan,
        middleware=[Middleware(RequestAuditMiddleware), Middleware(RateLimitMiddleware), Middleware(ComPDFCredentialMiddleware)],
        routes=[
            Route("/healthz", healthz),
            Route("/readyz", readyz),
            Route("/metrics", metrics),
            Mount("/mcp/conversion", conversion_server.streamable_http_app()),
            Mount("/mcp/ai", ai_server.streamable_http_app()),
            Mount("/mcp/pdf", pdf_server.streamable_http_app()),
            Mount("/mcp/generate", generate_server.streamable_http_app()),
            # The aggregate FastMCP app exposes its configured /mcp path at
            # the root, yielding a single URL suitable for MCP registries.
            Mount("/", aggregate_server.streamable_http_app()),
        ],
    )


app = create_app()


def main() -> None:
    uvicorn.run(
        "compdf_streaming_mcp.app:app",
        host=os.getenv("MCP_HOST", "0.0.0.0"),
        port=int(os.getenv("MCP_PORT", "8000")),
        reload=os.getenv("MCP_RELOAD", "false").lower() == "true",
    )


if __name__ == "__main__":
    main()
