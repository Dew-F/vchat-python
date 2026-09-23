from sqlmodel import Session

from app.users.errors import UserAlreadyExistsError, UserNotFoundError
from app.users.model import User, UserCreate
from app.users.password import hash_password
from app.users.repository import UserRepository


class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)
        self.session = session

    def create_user(self, data: UserCreate) -> User:
        with self.session.begin():
            if self.repository.get_by_username(data.username) is not None:
                raise UserAlreadyExistsError("username")

            if self.repository.get_by_email(data.email) is not None:
                raise UserAlreadyExistsError("email")

            user = User(
                username=data.username,
                email=data.email,
                password_hash=hash_password(data.password),
            )

            self.repository.add(user)

        return user

    def get_user(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundError(user_id)

        return user
