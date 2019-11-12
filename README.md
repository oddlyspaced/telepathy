# Telepathy
Telepathy is a python3 script based on Telethon which acts as a replacement for telegram.sh _which has stopped working in certain places due to the ISP's actually blocking telegram's web service api._


## Setting up
Before using the script, you must acquire the api id and api hash from telegram.org. Then create a config file name "telepathy" under ~/.config
**Example:**

`api_id=123456`

`api_hash=123123123123abcdabcdabcdabcd`

`username=oddlyspaced`

`session=default`

## Usage
After creating the config file, you can execute the telepathy.py in the following way -

`python3 telepathy.py "My Message"`

_As of now only text messages are supported_

## Using helper script
You can also place a script under /usr/bin containg the following content to access it from anywhere

`#!/bin/bash`

`cd /location/to/folder/`

`python3 telepathy.py $@`


