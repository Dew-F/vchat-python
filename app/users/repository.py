from sqlmodel import Session, select

from app.users.model import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)

        return self.session.exec(statement).first()

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)

        return self.session.exec(statement).first()

    def get_by_username(self, name: str) -> User | None:
        statement = select(User).where(User.username == name)

        return self.session.exec(statement).first()

    def add(self, user: User) -> None:
        self.session.add(user)
