"""Configurable bearer-token authentication for a protected MCP resource."""

from __future__ import annotations

import hmac
import json
import os
from dataclasses import dataclass
from typing import Any

from mcp.server.auth.provider import AccessToken
from mcp.server.auth.settings import AuthSettings


@dataclass(frozen=True)
class StaticTokenVerifier:
    """Verify pre-issued, rotatable service tokens without exposing their values."""

    tokens: dict[str, dict[str, Any]]

    async def verify_token(self, token: str) -> AccessToken | None:
        for configured, principal in self.tokens.items():
            if not hmac.compare_digest(token, configured):
                continue
            tenant_id = str(principal["tenant_id"])
            return AccessToken(
                token=token,
                client_id=tenant_id,
                subject=tenant_id,
                scopes=[str(scope) for scope in principal.get("scopes", ["compdf:invoke"])],
                claims={"tenant_id": tenant_id, "iss": os.environ["MCP_OAUTH_ISSUER_URL"]},
            )
        return None


def configured_auth() -> tuple[AuthSettings | None, StaticTokenVerifier | None]:
    """Return MCP OAuth resource-server settings when production auth is configured.

    ``MCP_STATIC_TOKENS_JSON`` intentionally supports several active tokens so
    operations can rotate a key by adding a replacement before retiring the
    old one.  The issuer remains an externally managed OAuth 2.1 issuer; this
    service validates the provisioned bearer credentials at its resource edge.
    """

    raw_tokens = os.getenv("MCP_STATIC_TOKENS_JSON", "").strip()
    environment = os.getenv("MCP_ENV", "development").lower()
    if not raw_tokens:
        if environment == "production":
            raise ValueError("MCP_STATIC_TOKENS_JSON is required when MCP_ENV=production.")
        return None, None

    issuer_url = os.getenv("MCP_OAUTH_ISSUER_URL", "").strip()
    resource_url = os.getenv("MCP_PUBLIC_URL", "").strip()
    if not issuer_url or not resource_url:
        raise ValueError("MCP_OAUTH_ISSUER_URL and MCP_PUBLIC_URL are required when authentication is enabled.")
    try:
        tokens = json.loads(raw_tokens)
    except json.JSONDecodeError as error:
        raise ValueError("MCP_STATIC_TOKENS_JSON must be a JSON object keyed by token value.") from error
    if not isinstance(tokens, dict) or not tokens:
        raise ValueError("MCP_STATIC_TOKENS_JSON must contain at least one token.")
    if any(not isinstance(token, str) or not token or not isinstance(principal, dict) or not principal.get("tenant_id") for token, principal in tokens.items()):
        raise ValueError("Each static token must map to an object with tenant_id and optional scopes.")
    scopes = [scope.strip() for scope in os.getenv("MCP_REQUIRED_SCOPES", "compdf:invoke").split(",") if scope.strip()]
    return (
        AuthSettings(issuer_url=issuer_url, resource_server_url=resource_url, required_scopes=scopes),
        StaticTokenVerifier(tokens=tokens),
    )
