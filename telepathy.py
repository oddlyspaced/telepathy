#!/bin/python3
from telethon import TelegramClient, events, sync
import sys
import subprocess

api_id = ""
api_hash = ""
username = ""
session = ""

# config file is located in ~/.config/telepathy
def read_config() :
    global api_id
    global api_hash
    global username
    global session
    f = open("/home/" + str(subprocess.check_output("whoami", shell=True))[2:-3] + "/.config/telepathy", "r")
    lines = list(f.readlines())
    for line in lines :
        line = str(line)
        if line.startswith("api_id") :
            api_id = line[line.index("=")+1:-1]
        if line.startswith("api_hash") :
            api_hash = line[line.index("=")+1:-1]
        if line.startswith("username") :
            username = line[line.index("=")+1:-1]
        if line.startswith("session") :
            session = line[line.index("=")+1:-1]

def help() :
    print("Usage: telepathy --username=<username> --message=<message>\nExample: telepathy --username=oddlyspaced --message=\"Test Message\"")

read_config()

client = TelegramClient(session + "_session", api_id, api_hash)
client.start()

args = list(sys.argv)
args.remove(args[0]) #removing script
for arg in args :
    client.send_message(username, arg)