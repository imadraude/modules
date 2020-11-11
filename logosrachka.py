import asyncio
from asyncio import wait, sleep

from .. import loader, utils
import telethon

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register



@register(outgoing=True, pattern="^.wedit (.*)")
async def tmeme(e):
    wedit = str(e.pattern_match.group(1))
    message = wedit.split()
    for _ in range(10):
        for mess in message:
            await e.edit(mess)
            await sleep(0.5)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#WEDIT\n"
            "Hm")

@register(outgoing=True, pattern="^.wlog (.*)")
async def tmemes(e):
    RuKeys = """аеуосхрАВСPОМНКТ"""
    EnKeys = """aeyocxpABCРOMHKT"""
    text = str(e.pattern_match.group(1))
    change = str.maketrans(RuKeys + EnKeys, EnKeys + RuKeys)
    texts = str.translate(text, change)
    for _ in range(20):
        await e.edit(texts)
        await sleep(0.2)
        await e.edit(text)
        await sleep(0.2)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#WLOG\n"
            "Hm")

@register(outgoing=True, pattern="^.cedit (.*)")
async def tmeme(e):
    cedit = str(e.pattern_match.group(1))
    message = cedit.replace(" ", "")
    for _ in range(10):
        for mess in message:
            await e.edit(mess)
            await sleep(0.1)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#CEDIT\n"
            "TSpam was executed successfully")
