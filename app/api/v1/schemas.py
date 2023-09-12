import uuid
from pydantic import BaseModel


class BotType(BaseModel):
    """Model for a bot"""

    token: str
    title: str
    tmp_chat_id: int


class BotCreateResponse(BotType):
    """Model for response on bot creation"""

    internal_id: uuid.UUID


class ChannelType(BaseModel):
    """Model for a channel"""

    bot_uuid: str
    channel_id: int
    channel_name: str


class ChannelCreateResponse(ChannelType):
    """Model for response on channel creation"""

    internal_id: str
