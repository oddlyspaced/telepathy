from telethon import TelegramClient, events, sync
from config import Config
import sys

api_id = Config.api_id
api_hash = Config.api_hash

client = TelegramClient('default_session', api_id, api_hash)
client.start()

username = ""
message = ""
args = list(sys.argv)
for arg in args :
    arg = str(arg)
    if arg.startswith("--username=") :
        username = arg[arg.index("=") + 1:]
    if arg.startswith("--message=") :
        message = arg[arg.index("=") + 1:]

if len(username) > 0 and len(message) > 0 :
    client.send_message(username, message)