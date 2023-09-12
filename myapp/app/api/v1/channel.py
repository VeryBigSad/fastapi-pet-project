from fastapi import APIRouter, HTTPException, Depends
from tortoise.transactions import atomic

from app.api.v1.schemas import ChannelCreate, ChannelResponse
from app.db.models import Channel

router = APIRouter()


@router.post("/channel", response_model=ChannelResponse)
@atomic()
async def add_channel(channel_data: ChannelCreate):
    channel = await Channel.create(**channel_data.model_dump())
    return channel


@router.get("/channel/{internal_id}", response_model=ChannelResponse)
async def get_channel(internal_id: str):
    channel = await Channel.get_or_none(internal_id=internal_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channel


@router.put("/channel/{internal_id}", response_model=ChannelResponse)
@atomic()
async def update_channel(internal_id: str, channel_data: ChannelCreate):
    channel = await Channel.get_or_none(internal_id=internal_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")

    for attr, value in channel_data.model_dump().items():
        setattr(channel, attr, value)

    await channel.save()

    return channel
