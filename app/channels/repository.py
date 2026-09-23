from sqlmodel import Session, select

from app.channels.model import Channel


class ChannelRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, channel_id: int) -> Channel | None:
        statement = select(Channel).where(Channel.id == channel_id)
        return self.session.exec(statement).first()

    def get_by_name(self, name: str) -> Channel | None:
        statement = select(Channel).where(Channel.name == name)
        return self.session.exec(statement).first()

    def add(self, channel: Channel) -> None:
        self.session.add(channel)
