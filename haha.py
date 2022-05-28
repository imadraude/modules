from asyncio import sleep
from random import choice, randint
from telethon import functions
from .. import loader, utils
import random
from userbot.events import register


@register(outgoing=True, pattern="^.haha (.*)")
async def haha(event):
    await event.delete()
    numb = int(event.pattern_match.group(1))
    reply = await event.get_reply_message()
    omg = ["АХ"]
    for _ in range(numb):
        lol = "".join([choice(omg) for _ in range(randint(6, 30))])
        if reply:
            await event.client.send_message(event.to_id, lol, reply_to=reply)
        else:
            await event.respond(lol)
