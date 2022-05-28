# CLOWN DESIGN HAHA
from .. import loader, utils
import telethon
from telethon import events, functions, types
import logging
import datetime
import time
from asyncio import sleep

logger = logging.getLogger(__name__)


def register(cb):
    cb(SpamAllMod())


@loader.tds
class SpamAllMod(loader.Module):
    """а)"""

    strings = {"name": "Спамальчик"}

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def spamallcmd(self, message):
        """.spamall <текст для спама> пишет всем юзерам в чате **Можете словить спам бан за такое**"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        users = await message.client.get_participants(message.to_id)
        if not args and not reply:
            await utils.answer(message, "а чем спамить будем, ало.")
            return
        await message.delete()
        for user in users:
            if not user.bot:
                try:
                    if reply:
                        if reply and not reply.text:
                            await message.client.send_file(str(user.username), reply)
                        else:
                            await message.client.send_message(
                                str(user.username), reply.text
                            )
                    else:
                        await message.client.send_message(str(user.username), args)
                except:
                    await sleep(0.1)
