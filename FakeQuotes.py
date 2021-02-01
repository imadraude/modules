# -*- coding: utf-8 -*-

# Hackintosh5 is my daddy

#Created by @droox hacked by @guslslakkaakdkabspy

# requires: Pillow requests

import logging
from .. import loader, utils
import telethon
import requests
import io
import json
import os
import PIL
logger = logging.getLogger(__name__)
@loader.tds
class drooxHuotesMod(loader.Module):
	"""ФЕЙКОВЫЕ КВОТЕСЫ ОТ @DROOX (ну и спай там идею придумал, хэш надыбал, вдохновил на создание короче)"""
	strings = {
		"name": "drooxHuotes",
		"silent_processing_cfg_doc": ("Process quote "
		                              "silently(mostly"
		                              " w/o editing)"),
		"api_endpoint_cfg_doc": "API endpoint URL",
		"module_endpoint_cfg_doc": "Module endpoint URL",
		"quote_limit_cfg_doc": "Limit for messages per quote",
		"max_width_cfg_doc": "Maximum quote width in pixels",
		"scale_factor_cfg_doc": "Quote quality (up to 5.5)",
		"square_avatar_cfg_doc": "Square avatar in quote",
		"text_color_cfg_doc": "Color of text in quote",
		"reply_line_color_cfg_doc": "Reply line color",
		"reply_thumb_radius_cfg_doc": ("Reply media thumbnail "
		                               "radius in pixels"),
		"admintitle_color_cfg_doc": "Admin title color",
		"message_radius_cfg_doc": "Message radius in px",
		"picture_radius_cfg_doc": "Media picture radius in px",
		"background_color_cfg_doc": "Quote background color",
		"quote_limit_reached": ("The maximum number "
		                        "of messages in "
		                        "multiquote - {}."),
		"processing": "<b>ща бует...</b>",
		"unreachable_error": "<b>какая то хуета с апи мишейза, помянем</b>",
		"server_error": "<b>а всё, пиздец</b>",
	}
	def __init__(self):
		# self.hash = hashlib.sha512(sys.modules.get(self.__module__).__loader__.data).hexdigest()
		# ХАХАХАХАХА МИШЕЙЗ СОСАТЬ СУКА ХАХАХАХАХА
		self.hash = "8253f1fa59415a6d105083e84b56939b5938d78989fe57990803e32f5619ebc20a2283d5a1c31b3f33fa4bd00876f73ab44a1de003586174a75dc371f22d2596"
		self.config = loader.ModuleConfig("API_ENDPOINT", "https://quotes.mishase.dev/create",
		                                  lambda: self.strings["api_endpoint_cfg_doc"],
		                                  "MODULE_ENDPOINT", "https://quotes.mishase.dev/f/module.py",
		                                  lambda: self.strings["module_endpoint_cfg_doc"],
		                                  "SILENT_PROCESSING", False,
		                                  lambda: self.strings["silent_processing_cfg_doc"],
		                                  "QUOTE_MESSAGES_LIMIT", 15,
		                                  lambda: self.strings["quote_limit_cfg_doc"],
		                                  "MAX_WIDTH", 384,
		                                  lambda: self.strings["max_width_cfg_doc"],
		                                  "SCALE_FACTOR", 5,
		                                  lambda: self.strings["scale_factor_cfg_doc"],
		                                  "SQUARE_AVATAR", False,
		                                  lambda: self.strings["square_avatar_cfg_doc"],
		                                  "TEXT_COLOR", "white",
		                                  lambda: self.strings["text_color_cfg_doc"],
		                                  "REPLY_LINE_COLOR", "white",
		                                  lambda: self.strings["reply_line_color_cfg_doc"],
		                                  "REPLY_THUMB_BORDER_RADIUS", 2,
		                                  lambda: self.strings["reply_thumb_radius_cfg_doc"],
		                                  "ADMINTITLE_COLOR", "#969ba0",
		                                  lambda: self.strings["admintitle_color_cfg_doc"],
		                                  "MESSAGE_BORDER_RADIUS", 10,
		                                  lambda: self.strings["message_radius_cfg_doc"],
		                                  "PICTURE_BORDER_RADIUS", 8,
		                                  lambda: self.strings["picture_radius_cfg_doc"],
		                                  "BACKGROUND_COLOR", "#162330",
		                                  lambda: self.strings["background_color_cfg_doc"])
	async def client_ready(self, client, db):
		self.client = client
	async def fqcmd(self, message):
		"""кто напишет эту команду тот сдохнет"""
		if not self.config["SILENT_PROCESSING"]:
			await utils.answer(
				message,
				self.strings(
					"processing",
					message
				)
			)
		args = utils.get_args_raw(message)
		reply = await message.get_reply_message()
		if len(spl_args := args.split(maxsplit=1)) == 2 and spl_args[0].startswith('@'):
			user = spl_args[0][1:]
			text = spl_args[1]
		elif reply:
			user = reply.from_id
			text = " ".join(spl_args)
		else:
			await utils.answer(message,
			                   '<b>ты тупой еблан сука введи правильно аргсы "@<юзернейм> <текст>" или "<реплай> <текст>" иначе никак дебил</b>')
			return
		user = await self.client.get_entity(user)
		name = telethon.utils.get_display_name(user)
		avatar = await self.client.download_profile_photo(user.id, "mishase_cache/")
		files = []
		msg = {
			"text": text,
			"reply": None,
			"entities": [],
			"author": {
				"id": str(user.id),
				"name": name,
				"adminTitle": ' ',
			}
		}
		if avatar:
			msg['author']['picture'] = {'file': f'@av{str(user.id).lstrip("-")}'}
			files.append(("files", (f'@av{str(user.id).lstrip("-")}', open(avatar, "rb"), "image/jpg")))
		else:
			files.append(("files", ("file", bytearray(), "text/text")))
		data = {
			"messages": [msg],
			"maxWidth": self.config["MAX_WIDTH"],
			"scaleFactor": self.config["SCALE_FACTOR"],
			"squareAvatar": self.config["SQUARE_AVATAR"],
			"textColor": self.config["TEXT_COLOR"],
			"replyLineColor": self.config["REPLY_LINE_COLOR"],
			"adminTitleColor": self.config["ADMINTITLE_COLOR"],
			"messageBorderRadius": self.config["MESSAGE_BORDER_RADIUS"],
			"replyThumbnailBorderRadius": self.config["REPLY_THUMB_BORDER_RADIUS"],
			"pictureBorderRadius": self.config["PICTURE_BORDER_RADIUS"],
			"backgroundColor": self.config["BACKGROUND_COLOR"],
		}
		try:
			req = await utils.run_sync(
				requests.post,
				self.config["API_ENDPOINT"],
				data={"data": json.dumps(data), "moduleHash": self.hash},
				files=files,
				timeout=100
			)
		except (requests.ConnectionError, requests.exceptions.Timeout):
			await clean_files()
			return await utils.answer(
				message,
				self.strings("unreachable_error", message)
			)
		await clean_files()
		if req.status_code >= 520:
			return await utils.answer(
				message,
				self.strings("unreachable_error", message)
			)
		if req.status_code >= 500:
			return await utils.answer(
				message,
				self.strings("server_error", message)
			)
		if req.status_code == 418:
			# А НЕ БУДЕТ 418. тока если мишейз не обновит модуль
			pass
		image = io.BytesIO()
		image.name = "hueta.webp"
		try:
			PIL.Image.open(io.BytesIO(req.content)).save(image, "WEBP")
			image.seek(0)
			return await utils.answer(message, image)
		except Exception as e:
			logger.error(e, exc_info=True)
			return await utils.answer(
				message,
				self.strings(
					"server_error",
					message
				)
			)

# а эту до пизды асинхронную функцию надо оставить, она держит весь модуль


async def clean_files():
	return os.system("rm -rf mishase_cache/*")


# тут была функция апдейт..... ПОМЯНЕМ ЕЁ НАХУЙ))))))))))000




# а тут была функция чек медиа или чёто типа того, еще куча всякого говна короче впизду весь этот шлак, нам оно не надо
