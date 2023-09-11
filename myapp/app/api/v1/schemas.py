from pydantic import BaseModel


class BotCreate(BaseModel):
    """Model for a bot"""
    token: str
    title: str
    tmp_chat_id: int


class BotResponse(BotCreate):
    """Model for response on bot creation"""
    internal_id: str  # UUID for internal representation of the bot


class ChannelCreate(BaseModel):
    """Model for a channel"""
    bot_uuid: str  # UUID of the associated bot
    channel_id: int
    channel_name: str


class ChannelResponse(ChannelCreate):
    """Model for response on channel creation"""
    internal_id: str

