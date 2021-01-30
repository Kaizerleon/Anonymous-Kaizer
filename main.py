from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("Hi, I am ANONYMOUS SENDER BOT.My Owener Is Kaveesha Poorna.\n\n"
                 "Just Forward me Some messages or\n"
                 "media and I will Anonymize the\n"
                 "sender.\n\n"
                 "Please Support The Developer\n"
                 "By Joining the Support @MATShub Channel👇👇")


if Credentials.START_MESSAGE is not None:
  START_TEXT = Credentials.START_MESSAGE
else:
  START_TEXT = DEFAULT_START
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,
                                message=START_TEXT,
                                buttons=[[Button.url("🤖 Deploy a clone 🤖","https://github.com/ShiranthaKellum/Anonymous-bot.git")],
                                         [Button.url("📢 Support Channel 📢","https://t.me/MATShub")],
                                         [Button.url("👨‍💻 Contact Owner 👨‍💻","https://t.me/Kaizerleon")]])                                                                 
    if event.message.media:
      await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass
    

with client:
  client.run_until_disconnected() 
