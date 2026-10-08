from fastapi import APIRouter, status

from app.auth.schemas import LoginRequest, TokenResponse
from app.auth.service import AuthService
from app.core.db.session import SessionDep

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, session: SessionDep):
    token = AuthService(session).login(data)
    return TokenResponse(access_token=token, token_type="bearer")
