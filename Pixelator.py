#Maded by clown.
#not licensed but i will fuck ur mom if ur going to use this code.
from .. import loader, utils
from PIL import Image
import io

def register(cb):
    cb(PixelatorMod())
class PixelatorMod(loader.Module):
    strings = {'name': 'Pixelator'}
    async def pixitcmd(self, event):
        """пикселятор. делает из арта пиксель арт. можно в качестве аргумента указать размеры пикселя. если аргумента нет то размер будет равен 16."""
        reply = await event.get_reply_message()
        if utils.get_args_raw(event):
            if utils.get_args_raw(event).isdigit():
                pixel = int(utils.get_args_raw(event))
            else:
                await event.edit("<b>аргумент указан не в интовом значении.</b>")
                return
        else:
            pixel = 16
        if not reply:
            await event.edit("<b>нет реплая на картинку/стикер.</b>")
            return
        pic = await check_media(event, reply)
        if not pic:
            await event.edit('<b>это не изображение, лол.</b>')
            return
        haha = pixelate(pic, pixel)
        await event.client.send_file(event.to_id, haha)
        await event.delete()

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

def pixelate(img, pixel_size):
    image = Image.open(io.BytesIO(img))
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    out = io.BytesIO()
    out.name = "pixed.png"
    image.save(out)
    return out.getvalue()