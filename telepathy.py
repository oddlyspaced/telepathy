#!/bin/python3
from telethon import TelegramClient, events, sync
from config import Config
import sys

# setting up
client = TelegramClient('default_session', Config.api_id, Config.api_hash)
client.start()

def help() :
    print("Usage: telepathy --username=<username> --message=<message>\nExample: telepathy --username=oddlyspaced --message=\"Test Message\"")

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
else :
    help()