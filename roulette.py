from .. import loader, utils
from random import randrange
from telethon import functions
from asyncio import sleep


def register(cb):
    cb(DancingwithdeathMod())


class DancingwithdeathMod(loader.Module):
    strings = {"name": "Dancing with death"}

    async def deadplaycmd(self, die):
        args = utils.get_args_raw(die)
        if args == "правила":
            await die.edit(
                "Правила просты \n\n>есть рулетка которая рандомит число от 1 до 6 \n\n>есть твое число которое тоже находится в диапазоне от 1 до 6\n\n>при условии если эти числа совпадают - ты умираешь\n\n>в остальных случаях ты остаешься в живых\n\n\n->как заполнять анкету дьявола - .deadplay <число от 1 до 6> пример - .deadplay 5"
            )
            return
        if int(args) > 0 and int(args) < 7:
            await die.edit("рулетка запустилась (0)")
            await sleep(1)
            await die.edit("рулетка запустилась (1)")
            await sleep(1)
            await die.edit("рулетка запустилась (2)")
            await sleep(1)
            await die.edit("рулетка запустилась (3)")
            await sleep(1)
            deadnumber = randrange(1, 6)
            if deadnumber == int(args):
                await die.edit("<b>*звук выстрела*</b>")
            else:
                await die.edit(
                    f"в этот раз тебе повезло, твое число — <b>{args}</b>, число смерти — <b>{deadnumber}</b>"
                )
        else:
            await die.edit("числа могут быть только от 1 до 6")
            return
