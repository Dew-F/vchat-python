from fastapi import APIRouter, status

from app.channels.model import ChannelCreate, ChannelPublic
from app.channels.service import ChannelService
from app.db.session import SessionDep

router = APIRouter(prefix="/api/v1/channel", tags=["channel"])


@router.post("", response_model=ChannelPublic, status_code=status.HTTP_201_CREATED)
def create_channel(data: ChannelCreate, session: SessionDep):
    service = ChannelService(session)
    return service.create_channel(data)


@router.get("/{channel_id}", response_model=ChannelPublic)
def get_channel(channel_id: int, session: SessionDep):
    service = ChannelService(session)
    return service.get_channel(channel_id)
