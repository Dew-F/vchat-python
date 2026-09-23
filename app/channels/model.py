from datetime import datetime

from sqlalchemy import func
from sqlmodel import Field, SQLModel


class ChannelBase(SQLModel):
    name: str = Field(min_length=3, max_length=50)
    is_voice: bool = Field(default=False)
    is_private: bool = Field(default=False)
    is_direct: bool = Field(default=False)


class ChannelId(SQLModel):
    id: int | None = Field(
        default=None,
        primary_key=True,
    )


class Channel(ChannelBase, ChannelId, table=True):
    __tablename__ = "channels"

    created_at: datetime = Field(
        nullable=False,
        sa_column_kwargs={
            "server_default": func.current_timestamp(),
        },
    )


class ChannelCreate(ChannelBase):
    pass


class ChannelPublic(ChannelBase, ChannelId):
    created_at: datetime
