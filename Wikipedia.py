#by @imadraude

from .. import loader, utils
import requests
import wikipedia


def register(cb):
    cb(WikipediaMod())
    
class WikipediaMod(loader.Module):
    """Википедия, ачё"""
    strings = {'name': 'Wikipedia'}

    async def wikicmd(self, message):
        """.wiki <искомое слово>"""
        
        args = utils.get_args_raw(message)
        split_args = args.split()

        lang = split_args[0]
        text = args.split(" ", 1)[1]

        if not args:
            await message.edit("<b>Википедия не настолько умная, чтобы искать ничего.</b>")

        await message.edit("<b>Ищем...</b>")
        
        try:    
            wikipedia.set_lang(lang)
            summ = wikipedia.summary(args)

            await message.edit(f"<i>• {summ}</i>")
        except Exception as e:
            return await message.edit(str(e))

    async def wikiscmd(self, message):
        """.wikis <искомое слово>, выдаёт возможные результаты"""

        args = utils.get_args_raw(message)

        try:
            lang = split_args[0]
            text = args.split(" ", 1)[1]

        except:
            lang = "ru"
            text = args

        if not args:
            await message.edit("<b>Мне нечего искать, введи что-нибудь.</b>")

        await message.edit("<b>Ищем...</b>")
        
        try:    
            wikipedia.set_lang(lang)
            search = "<code>" + '\n'.join([f"<code>{_}</code>" for _ in wikipedia.search(args)]) + "</code>"

            await message.edit(f"<i>• Результаты:\n\n</i>{search}")
        except Exception as e:
            return await message.edit(str(e))

    async def wikirucmd(self, message):
        """.wikiru <искомое слово>"""
        
        args = utils.get_args_raw(message)
        split_args = args.split()

        if not args:
            await message.edit("<b>Википедия не настолько умная, чтобы искать ничего.</b>")

        await message.edit("<b>Ищем...</b>")
        
        try:    
            wikipedia.set_lang("ru")
            summ = wikipedia.summary(args)
            
            await message.edit(f"<i>• {summ}</i>")
        except Exception as e:
            return await message.edit(str(e))

