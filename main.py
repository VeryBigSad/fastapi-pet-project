from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.v1.bot import router as bot_router
from app.api.v1.channel import router as channel_router
from app.db.config import TORTOISE_ORM

app = FastAPI()

# Include the API routers
app.include_router(bot_router, prefix="/v1")
app.include_router(channel_router, prefix="/v1")

# Configure Tortoise ORM
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # Auto-generate database schemas
    add_exception_handlers=True,  # Add exception handlers
)

if __name__ == "__main__":
    import uvicorn

    # Run the ASGI server using UVicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)