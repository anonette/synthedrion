"""Authentication module for production API security."""

import os
from typing import Optional

from fastapi import Header, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer(auto_error=False)


def verify_token(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security),
) -> str:
    """Verify the API token for protected endpoints."""
    # In development, allow no auth
    if os.getenv("PRODUCTION", "false").lower() != "true":
        return "dev-token"
    
    if not credentials:
        raise HTTPException(
            status_code=403,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = credentials.credentials
    expected_token = os.getenv("API_TOKEN", "")
    
    if not expected_token:
        raise HTTPException(
            status_code=500,
            detail="API_TOKEN not configured",
        )
    
    if token != expected_token:
        raise HTTPException(
            status_code=403,
            detail="Invalid authentication token",
        )
    
    return token


def optional_token(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security),
) -> Optional[str]:
    """Optional token verification for public endpoints with rate limiting."""
    if not credentials:
        return None
    
    try:
        return verify_token(credentials)
    except HTTPException:
        return None


def require_roundtable_operator(x_roundtable_token: str | None = Header(default=None)) -> str:
    """Protect mutating roundtable endpoints with a shared operator token."""
    expected_token = os.getenv("ROUNDTABLE_OPERATOR_TOKEN", "")

    if not expected_token:
        raise HTTPException(status_code=500, detail="ROUNDTABLE_OPERATOR_TOKEN not configured")

    if x_roundtable_token != expected_token:
        raise HTTPException(status_code=401, detail="Operator token required")

    return x_roundtable_token
