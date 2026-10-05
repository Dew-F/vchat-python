from sqlalchemy import select
from sqlalchemy.orm import Session

from app.users.models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)

        return self.session.execute(statement).scalar_one_or_none()

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)

        return self.session.execute(statement).scalar_one_or_none()

    def get_by_username(self, name: str) -> User | None:
        statement = select(User).where(User.username == name)

        return self.session.execute(statement).scalar_one_or_none()

    def add(self, user: User) -> None:
        self.session.add(user)
