from asyncio import sleep
import random
from telethon import functions, types, events
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils

def register(cb):
    cb(CurrencyMod())

class CurrencyMod(loader.Module):
    strings = {'name': 'Currency'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def curcmd(self, event):
        chat = '@exchange_rates_vsk_bot'
        args = utils.get_args_raw(event)
        if args:
            arg = args
        else:
            arg = None
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1210425892))
                if arg:
                    await event.client.send_message(chat, f'{arg}')
                else:
                    await message.edit("<b>Введи нужную валюту!</b>")
                response = await response
            except YouBlockedUserError:
                await event.edit('<code>Разблокируй @exchange_rates_vsk_bot</code>')
                return
            await event.edit(response.text)