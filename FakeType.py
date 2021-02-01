from .. import loader, utils
from asyncio import sleep
def register(cb):
    cb(FakeTypeMod())
class FakeTypeMod(loader.Module):
    """тайпим..."""
    strings = {'name': 'Тайпер ахах'}
    async def typingcmd(self, message):
        args = utils.get_args_raw(message)
        if not args.isdigit():
            return await message.edit("инт?")
        async with message.client.action(message.to_id, 'typing'):
            await sleep(int(args))