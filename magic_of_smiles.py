from .. import loader
from asyncio import sleep


@loader.tds
class HeartsMod(loader.Module):
    strings = {"name": "Magic of smiles"}

    @loader.owner
    async def heartscmd(self, message):
        for _ in range(10):
            for heart in ["🤎", "💛", "💚", "🤍", "💜", "🖤", "❤"]:
                await message.edit(heart)
                await sleep(0.3)

    async def moonscmd(self, message):
        for _ in range(10):
            for moon in ["�", "�"]:
                await message.edit(moon)
                await sleep(0.3)

    async def moons2cmd(self, message):
        for _ in range(10):
            for moon2 in ["🌕", "🌖", "🌗", "🌘", "🌑", "�", "�", "�"]:
                await message.edit(moon2)
                await sleep(0.3)

    async def earthcmd(self, message):
        for _ in range(10):
            for earth in ["🌎", "🌍", "🌏"]:
                await message.edit(earth)
                await sleep(0.5)

    async def clockscmd(self, message):
        for _ in range(12):
            for clock in ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]:
                await message.edit(clock)
                await sleep(0.3)

    async def policecmd(self, message):
        for _ in range(20):
            for police in [
                "🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵",
                "🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴",
            ]:
                await message.edit(police)
                await sleep(0.3)

    async def dickcmd(self, message):
        await message.edit(
            "\u2060      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿"
        )
        await sleep(1)
        await message.edit(
            "\u2060    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿"
        )
        await sleep(1)
        await message.edit(
            "\u2060  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    🗿🗿🗿\n     "
            "🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿"
        )
        await sleep(1)
        await message.edit(
            "\u2060💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    "
            "🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿"
        )
        await sleep(1)
        await message.edit(
            "\u2060💦💦\n💦\n💦\n  💦\n    💦\n      💦\n❤️❤️❤️\n🗿🗿🗿\n  🗿🗿🗿\n    "
            "🗿🗿🗿\n     🗿🗿🗿\n       🗿🗿🗿\n        🗿🗿🗿\n         🗿🗿🗿\n          🗿🗿🗿\n          🗿🗿🗿\n      🗿🗿🗿🗿\n 🗿🗿🗿🗿🗿🗿\n 🗿🗿🗿  🗿🗿🗿\n    🗿🗿       🗿🗿"
        )
