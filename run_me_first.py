# ############################################################################################
# This file is used to create a session file for the telegram client
# You need to create a .env file in the same directory as this file
# and add the following variables:
# 
# TELETHON_SESSION_NAME = "your_session_name"
# TELEGRAM_API_ID = "your_api_id"
# TELEGRAM_API_HASH = "your_api_hash"
# 
# If the process is successful, a session file will be created in the same directory
# for example if you set TELETHON_SESSION_NAME = "my_session", 
# a file named my_session.session will be created in the same directory
# and you will receive a message from yourself in telegram, take a look to Saved Messages
# ############################################################################################

import os
from dotenv import dotenv_values
from telethon import TelegramClient, events
from config import config
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)


# Load your account from the session file if it exists
session_name = config["TELETHON_SESSION_NAME"]
# Your telegram api id and api hash
api_id = config["TELEGRAM_API_ID"]
api_hash = config["TELEGRAM_API_HASH"]

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    # Getting information about yourself
    logging.info("Getting information about yourself")
    me = await client.get_me()

    username = me.username # type: ignore
    print("Username:", username)
    print("Phone:", me.phone) # type: ignore

    logging.info("Sending message to myself")
    await client.send_message('me', 'Hello, myself!')



@client.on(events.NewMessage)  # type: ignore
async def my_event_handler(event):
    logging.info(event.raw_text)
    # if 'hello' in event.raw_text:
    #     await event.reply('hi!')
    



with client:
    client.start()
    client.loop.run_until_complete(main())
    client.loop.run_forever()