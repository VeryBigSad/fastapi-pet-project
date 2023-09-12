from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "bot" (
    "internal_id" CHAR(36) NOT NULL  PRIMARY KEY,
    "token" VARCHAR(255) NOT NULL,
    "title" VARCHAR(32) NOT NULL,
    "tmp_chat_id" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "channel" (
    "internal_id" CHAR(36) NOT NULL  PRIMARY KEY,
    "bot_uuid" CHAR(36) NOT NULL,
    "channel_id" INT NOT NULL,
    "channel_name" VARCHAR(32) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
