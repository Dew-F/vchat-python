from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.errors import InvalidTokenError
from app.core.db.session import SessionDep
from app.core.security.jwt import decode_access_token
from app.users.models import User
from app.users.repository import UserRepository

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(security)],
    session: SessionDep,
) -> User:
    if credentials is None:
        raise InvalidTokenError()

    user_id = decode_access_token(credentials.credentials)
    if user_id is None:
        raise InvalidTokenError()

    user = UserRepository(session).get_by_id(user_id)
    if user is None:
        raise InvalidTokenError()

    return user
