from tortoise import fields
from tortoise.models import Model


class Bot(Model):
    internal_id = fields.UUIDField(pk=True)
    token = fields.CharField(max_length=255)
    title = fields.CharField(max_length=32)
    tmp_chat_id = fields.IntField()


class Channel(Model):
    internal_id = fields.UUIDField(pk=True)
    bot_uuid = fields.UUIDField()
    channel_id = fields.IntField()
    channel_name = fields.CharField(max_length=32)
