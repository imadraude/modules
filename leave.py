from .. import loader, utils
from asyncio import sleep
from telethon.tl.functions.channels import LeaveChannelRequest


@loader.tds
class LeaveMod(loader.Module):
    strings = {"name": "ливаю нахуй"}

    @loader.sudo
    async def leavecmd(self, message):
        """.leave"""
        if not message.chat:
            await message.edit("<b>Дурка блядь</b>")
            return
        text = utils.get_args_raw(message)
        if not text:
            text = "До связи."
        if text.lower() == "del":
            await message.delete()
        else:
            await message.edit(f"<code>{text}</code>")
            await sleep(1)
            await message.client(LeaveChannelRequest(message.chat_id))
