import logging 
from .. import loader 
from telethon.tl.types import Message 
 
@loader.tds 
class imgayMod(loader.Module): 
 """ugh...""" 
 strings = {"name": "voluntarily and being of sound mind I declare that I am gay"} 
 
 async def watcher(self, message): 
  if isinstance(message, Message): 
   if message.sender_id == (await message.client.get_me()).id: 
    await message.delete()