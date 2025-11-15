from pydantic import BaseModel

from typing import Optional


# =========================
# CHANNEL SCHEMAS
# =========================
class ChannelBase(BaseModel):
    channel_id: int
    username: str


class ChannelCreate(ChannelBase):
    pass


class ChannelUpdate(BaseModel):
    channel_id: Optional[int] = None
    username: Optional[str] = None


class ChannelRead(ChannelBase):
    id: int