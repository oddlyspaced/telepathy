from telethon import TelegramClient, events, sync
from config import Config

api_id = Config.api_id
api_hash = Config.api_hash

client = TelegramClient('default_session', api_id, api_hash)
client.start()