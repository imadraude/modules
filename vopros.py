from .. import loader, utils
import random
def register(cb):
	cb(VoprosMod())
class VoprosMod(loader.Module):
	"""Vopros"""
	strings = {'name': 'Vopros'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def voproscmd(self, message):
		""".vopros действие
		"""
		do = utils.get_args_raw(message)
		rnd = random.choice(["Определённо да", "Нет", "Не уверен", "Не думаю", "Возможно", "Да", "Определённо нет", "Не знаю", "Да", "Не уверен", "Нет", "Определённо да", "Нет", "Возможно", "Да", "Определённо нет", "Не знаю", "Не думаю", "Да", "Нет", "Не знаю", "Возможно", "Не думаю", "Определённо да", "Определённо нет","Не уверен", "Определённо да", "Не уверен", "Да", "Не знаю", "Возможно", "Не думаю", "Нет", "Определённо нет", "Нет", "Определённо да", "Возможно", "Не думаю", "Определённо нет","Не уверен", "Да", "Не знаю", ])
		await message.edit(f"<b>{do}</b>\n\n<code>{rnd}</code>")


		
