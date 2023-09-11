from fastapi import APIRouter, HTTPException, Depends
from tortoise.transactions import atomic

from app.api.v1.schemas import BotCreate, BotResponse
from app.db.models import Bot

router = APIRouter()

@router.post("/bot", response_model=BotResponse)
@atomic()
async def add_bot(bot_data: BotCreate):
    bot = await Bot.create(**bot_data.dict())
    return bot

@router.get("/bot/{internal_id}", response_model=BotResponse)
async def get_bot(internal_id: str):
    bot = await Bot.get_or_none(internal_id=internal_id)
    if not bot:
        raise HTTPException(status_code=404, detail="Bot not found")
    return bot


@router.put("/bot/{internal_id}", response_model=BotResponse)
@atomic()
async def update_bot(internal_id: str, bot_data: BotCreate):
    bot = await Bot.get_or_none(internal_id=internal_id)
    if not bot:
        raise HTTPException(status_code=404, detail="Bot not found")

    # Update bot attributes
    for attr, value in bot_data.dict().items():
        setattr(bot, attr, value)
    
    await bot.save()
    
    return bot