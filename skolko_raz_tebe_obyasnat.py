#Created by clown :/
#pm - @guslslakkaakdkab
import telethon
from .. import loader, utils
import os
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import re
import io
from io import BytesIO
from textwrap import wrap
import random

def register(cb):
    cb(SkolkoMod())

class SkolkoMod(loader.Module):
    """Согласен"""
    strings = {'name': 'Сколько раз блять тебе обьяснять'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def skokcmd(self, message):
        """.skok <реплай на изображение.>"""

        reply = await message.get_reply_message()
        if not reply:
            await message.edit("где реплай на медиа.")
        else:
            pic = await check_media(message, reply)
            if not pic:
                await utils.answer(message, 'нет изображения.')
                return
            what = haha(pic)
            await message.delete()
            await message.client.send_file(message.to_id, what)

def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def haha(image):
    pics = requests.get("https://github.com/SpyderJabro/SpYD3R/blob/master/photo.jpg?raw=true")
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGBA")
    lol(img, image, (20, 240), 150)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out)
    return out.getvalue()

async def check_media(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_media(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None



