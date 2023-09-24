from telethon.tl.custom.message import Message
from telethon.tl.custom.conversation import Conversation

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


async def send_message(conv: Conversation, message):
    logging.info("Sending: {}".format(message))
    await conv.send_message(message)

async def get_response(conv: Conversation):
    resp: Message = await conv.get_response()
    logging.info("Response: {}".format(str(resp.raw_text)))
    return resp

async def cmd_reset_all(conv: Conversation):
    await send_message(conv, "/reset all")
    resp: Message = await get_response(conv)
    assert "reset" in str(resp.raw_text)