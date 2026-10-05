from sqlalchemy import select
from sqlalchemy.orm import Session

from app.channels.models import Channel


class ChannelRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, channel_id: int) -> Channel | None:
        statement = select(Channel).where(Channel.id == channel_id)
        return self.session.execute(statement).scalar_one_or_none()

    def get_by_name(self, name: str) -> Channel | None:
        statement = select(Channel).where(Channel.name == name)
        return self.session.execute(statement).scalar_one_or_none()

    def add(self, channel: Channel) -> None:
        self.session.add(channel)
