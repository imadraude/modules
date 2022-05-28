from telethon import functions, types
from asyncio import sleep
from .. import loader, utils
from PIL import Image
import io


def register(cb):
    cb(CrossMod())


class CrossMod(loader.Module):
    """cross all"""

    strings = {"name": "Cross"}

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def crosscmd(self, message):
        """.cross <reply to file>"""
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b>А что зачеркнуть?</b>")
            return
        client = message.client
        im = io.BytesIO()
        await client.download_file(reply, im)
        im = Image.open(im)
        width, heigth = im.size
        center = min(width, heigth)
        im = im.crop(
            (
                (width - center) // 2,
                (heigth - center) // 2,
                (width + center) // 2,
                (heigth + center) // 2,
            )
        )
        line = Image.new("RGBA", (width, heigth // 6), (255, 0, 0, 255))
        line_one = line.rotate(45, expand=True, fillcolor=None).resize(im.size)
        line_two = line.rotate(-45, expand=True, fillcolor=None).resize(im.size)
        line_two.paste(line_one, (0, 0), line_one)
        cross = Image.new("RGBA", im.size, (255, 255, 255, 255))
        cross.paste(line_two, (0, 0), line_two)
        cross.putalpha(150)
        im.paste(cross, (0, 0), cross)
        output = io.BytesIO()
        output.name = "output.png"
        im.save(output)
        output.seek(0)
        await client.send_file(message.to_id, output, reply_to=reply)
        await message.delete()
        await sleep(5)
