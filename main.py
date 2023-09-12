from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.v1.bot import router as bot_router
from app.api.v1.channel import router as channel_router
from app.db.config import TORTOISE_ORM
from middlewares.authorization import authorization_middleware

app = FastAPI()

# routes
app.include_router(bot_router, prefix="/api")
app.include_router(channel_router, prefix="/api")

# middleware
app.middleware("http")(authorization_middleware)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn

    # Run the ASGI server using UVicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9176, reload=True)
