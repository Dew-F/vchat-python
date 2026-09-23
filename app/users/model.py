from datetime import datetime, timezone

from sqlmodel import SQLModel, Field, func


class UserBase(SQLModel):
    username: str = Field(min_length=3, max_length=20)
    email: str = Field(min_length=5, max_length=100)


class UserId(SQLModel):
    id: int | None = Field(
        default=None,
        primary_key=True,
    )


class User(UserBase, UserId, table=True):
    __tablename__ = "users"

    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(
        nullable=False,
        sa_column_kwargs={
            "server_default": func.current_timestamp(),
        },
    )


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class UserPublic(UserBase, UserId):
    created_at: datetime
