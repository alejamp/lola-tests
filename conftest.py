import pytest_asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.custom.message import Message
from config import config



pytest_plugins = ('pytest_asyncio',)

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

# Load your account from the session file if it exists
session_name = config["TELETHON_SESSION_NAME"]
# Your telegram api id and api hash
api_id = config["TELEGRAM_API_ID"]
api_hash = config["TELEGRAM_API_HASH"]


@pytest_asyncio.fixture(scope="session")
async def client():


    logging.info("Creating client")
    client = TelegramClient(session_name, api_id, api_hash)

    # Connect to the server
    await client.connect()
    logging.info("Connected to Telegram")
    # Issue a high level command to start receiving message
    me = await client.get_me()
    logging.info("Logged in as: {}".format(me.username))
    # Fill the entity cache
    await client.get_dialogs()
    logging.info("Dialogs loaded")

    yield client

    await client.disconnect() # type: ignore
    await client.disconnected

