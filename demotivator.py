#by @krabodyan
from telethon.events import NewMessage
from telethon.errors.rpcerrorlist import YouBlockedUserError
from asyncio.exceptions import TimeoutError, CancelledError
from .. import loader, utils


def register(cb):
	cb(DemotivatorMod())


class DemotivatorMod(loader.Module):
    """Демотиватор от крабодяна"""

    strings = {'name': 'Демотиватор'}
    
    async def client_ready(self, client, _):
        self.client = client
        
    async def demcmd(self, message):
        """ .dem <текст> <реплай на медиа>"""

        reply = await message.get_reply_message()
        if not reply or not reply.media or not any([
        	True for _ in ('sticker', 'photo', 'video')
        	if getattr(reply, _, None) is not None
        	]):
        	return await message.edit("<b>нужен реплай на фотку!</b>")
        if reply.file.size / 1024 / 1024 > 1:
        	return await message.edit("<b>бот принимает видео до 1 мб (но можно скинуть бабла автору бота на сервер и будет до 5)</b>")


        args = utils.get_args_raw(message) or reply.message
        if not args:
        	return await message.edit('<b>укажи аргументы после команды...</b>')

        if len(args) > 300:
        	return await message.edit("<b>бот принимает текст длинной до 200 символов</b>")

        chat = "IvIy_bot"
        await message.edit("<b>демотивирую...</b>")
        async with self.client.conversation(chat, timeout=30) as conv:
            try:
                response = conv.wait_event(NewMessage(incoming=True, from_users=chat))
                msg = await message.client.send_file(chat, reply.media)
                await msg.reply(f"/demoti {args}")
                response = await response
                if not response.media:
                	response = conv.wait_event(NewMessage(incoming=True, from_users=chat))
                	response = await response
                

            except YouBlockedUserError:
                return await message.edit(f'<b>Разблокируй @{chat}</b>')

            except (TimeoutError, CancelledError):
            	return await message.edit("<b>бот не ответил => @krabodyan ебланище</b>")
            
            await self.client.send_file(message.to_id, response.media, reply_to=reply)
            await message.delete()
            
