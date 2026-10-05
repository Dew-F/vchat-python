from sqlalchemy.orm import Session

from app.channels.errors import ChannelAlreadyExistsError, ChannelNotFoundError
from app.channels.models import Channel
from app.channels.repository import ChannelRepository
from app.channels.schemas import ChannelCreate


class ChannelService:
    def __init__(self, session: Session):
        self.repository = ChannelRepository(session)
        self.session = session

    def create_channel(self, data: ChannelCreate) -> Channel:
        with self.session.begin():
            if self.repository.get_by_name(data.name) is not None:
                raise ChannelAlreadyExistsError("name")

            channel = Channel(
                name=data.name,
                is_voice=data.is_voice,
                is_private=data.is_private,
                is_direct=data.is_direct,
            )

            self.repository.add(channel)

        return channel

    def get_channel(self, channel_id: int) -> Channel:
        channel = self.repository.get_by_id(channel_id)

        if channel is None:
            raise ChannelNotFoundError(channel_id)

        return channel
