from sqlalchemy.orm import Session

from app.auth.errors import InvalidCredentialsError
from app.auth.schemas import LoginRequest
from app.core.security.jwt import create_access_token
from app.users.password import verify_password
from app.users.repository import UserRepository


class AuthService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)
        self.session = session

    def login(self, data: LoginRequest) -> str:
        user = self.repository.get_by_username(data.username)
        if user is None:
            raise InvalidCredentialsError()

        if not verify_password(data.password, user.password_hash):
            raise InvalidCredentialsError()

        return create_access_token(user.id)
