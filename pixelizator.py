from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import io
from PIL import Image, ImageOps
from telethon.tl.types import DocumentAttributeFilename
import logging
import random

logger = logging.getLogger(__name__)

def register(cb):
	cb(PixelizatorMod())


@loader.tds
class PixelizatorMod(loader.Module):
	"""Pixelizator"""
	strings = {
		"name": "Pixelizator"
	}

	async def client_ready(self, client, db):
		self.client = client
	
	
	@loader.sudo
	async def pixcmd(self, message):
		""".pix <reply to photo>"""
		soap = 3
		a = utils.get_args(message)
		if a:
			if a[0].isdigit():
				soap = int(a[0])
				if soap <= 0:
					soap = 3
		
		if message.is_reply:
			reply_message = await message.get_reply_message()
			data = await check_media(reply_message)
			if isinstance(data, bool):
				await utils.answer(message, "<code>Reply to pic or stick!</code>")
				return
		else:
			await utils.answer(message, "<code>Reply to pic or stick!</code>")
			return
		
		await message.edit("Pixelizing...")
		file = await self.client.download_media(data, bytes)
		media = await Soaping(file, soap)
		await message.delete()
		
		await message.client.send_file(message.to_id, media)
		
	
		

async def Soaping(file, soap):
	img = Image.open(io.BytesIO(file))
	(x, y) = img.size
	img = img.resize((x//soap, y//soap), Image.BOX)
	img = img.resize((x, y), Image.BOX)
	soap_io = io.BytesIO()
	soap_io.name = "image.jpeg"
	img = img.convert("RGB")
	img.save(soap_io, "JPEG", quality=100)
	soap_io.seek(0)
	return soap_io
	

async def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.document:
			if DocumentAttributeFilename(file_name='AnimatedSticker.tgs') in reply_message.media.document.attributes:
				return False
			if reply_message.gif or reply_message.video or reply_message.audio or reply_message.voice:
				return False
			data = reply_message.media.document
		else:
			return False
	else:
		return False

	if not data or data is None:
		return False
	else:
		return data
