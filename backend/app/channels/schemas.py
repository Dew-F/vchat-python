from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ChannelBase(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    is_voice: bool = False
    is_private: bool = False
    is_direct: bool = False


class ChannelCreate(ChannelBase):
    pass


class ChannelPublic(ChannelBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
