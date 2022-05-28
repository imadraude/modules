from .. import loader
from asyncio import sleep
from random import randint


@loader.tds
class autobattleMod(loader.Module):
    strings = {"name": "ebawy kawy"}

    async def watcher(self, message):
        if message.chat_id == -1001373295507 and message.sender_id == 701686415:
            if "Атакуем" in message.raw_text:
                await sleep(randint(30, 60))
                await message.click()
                await message.client.send_message("@citywars2_bot", "/buy_set_3")
            elif "Встаём в" in message.raw_text:
                await sleep(randint(30, 60))
                await message.click()
                await message.client.send_message("@citywars2_bot", "/buy_set_3")
