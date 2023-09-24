import asyncio
import pytest
pytest_plugins = ('pytest_asyncio',)
from telethon import TelegramClient
from telethon.tl.custom.message import Message

# import helpers
from utils import get_response, send_message
from smart_asserts import nlp_assert

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


bot_name = "@botFather"
timeout = 40

# WORK AROUND pytest using async
# Add this code to the test files
# https://stackoverflow.com/questions/56236637/using-pytest-fixturescope-module-with-pytest-mark-asyncio
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
# ------------------------------------------



# TEST CASE:
@pytest.mark.asyncio
async def test_botFather_mybots_command(client: TelegramClient):
    # Create a conversation
    async with client.conversation(bot_name, timeout=timeout) as conv:
        

        # Send message to bot
        await send_message(conv, "/mybots")

        # Get response
        resp: Message = await get_response(conv)

        # Check if the response says the code is invalid
        eval, o, e = nlp_assert(resp.message, "Is asking to choose a bot?. Answer only true or false", "true")
        assert eval

        
        
