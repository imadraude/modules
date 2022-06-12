# by @imadraude

from .. import loader, utils
import requests
import wikipedia


def register(cb):
    cb(WikipediaMod())


class WikipediaMod(loader.Module):
    """Википедия, ачё"""

    strings = {"name": "Wikipedia"}

    async def wikiscmd(self, message):
        """.wikis <искомое слово>, выдаёт возможные результаты"""

        args = utils.get_args_raw(message)
        split_args = args.split()

        try:
            lang = split_args[0]
            text = args.split(" ", 1)[1]
        except:
            lang = "ru"
            text = args

        if not text:
            return await message.edit("<b>Не указан запрос.</b>")

        await message.edit("<b>Ищем...</b>")

        try:
            wikipedia.set_lang(lang)
            search = (
                "<code>"
                + "\n".join([f"<code>{_}</code>" for _ in wikipedia.search(args)])
                + "</code>"
            )

            await message.edit(f"<i>• Результаты:\n\n</i>{search}")
            # перечислить все возможные ошибки
        except wikipedia.exceptions.DisambiguationError as e:
            await message.edit(
                f"<i>• Несколько вариантов для запроса:</i>\n\n<code>{e.options}</code>"
            )
        except wikipedia.exceptions.PageError as e:
            return await message.edit("<b>По данному запросу ничего не найдено.</b>")
        except wikipedia.exceptions.WikipediaException as e:
            return await message.edit(f"<b>Произошла ошибка:</b>\n\n<code>{e}</code>")

    async def wikirucmd(self, message):
        """.wikiru <искомое слово>"""

        args = utils.get_args_raw(message)

        if not args:
            return await message.edit("<b>Не указан запрос.</b>")

        await message.edit("<b>Ищем...</b>")

        try:
            wikipedia.set_lang("ru")
            sum = wikipedia.summary(args)
            await message.edit(f"<i>• {sum}</i>")
        except wikipedia.exceptions.DisambiguationError as e:
            await message.edit(
                f"<i>• Несколько вариантов для запроса:</i>\n\n<code>{e.options}</code>"
            )
        except wikipedia.exceptions.PageError as e:
            return await message.edit("<b>По данному запросу ничего не найдено.</b>")
        except wikipedia.exceptions.WikipediaException as e:
            return await message.edit(f"<b>Произошла ошибка:</b>\n\n<code>{e}</code>")
