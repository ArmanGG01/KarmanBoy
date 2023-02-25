import os
import re
from platform import python_version as y
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Kynan.events import register
from Kynan import telethn as tbot


PHOTO = "https://telegra.ph/file/22f6ad3a94a5b73833057.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"┏━━━━━━━━━━━━━━━━━━━━┓\n"
  TEXT += f"┠➣ **ҡᴋꝛλɴ ꭙ ꝛσʙσᴛ.** \n"
  TEXT += f"┠➣ **ᴍʏ ᴏᴡɴᴇʀ : [↻˹ҡʏɴλɴ˼༗](https://t.me/Riizzvbss)**\n"
  TEXT += f"┠➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`\n"
  TEXT += f"┠➣ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
  TEXT += f"┠➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"┠➣ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n"
  TEXT += "┗━━━━━━━━━━━━━━━━━━━━┛"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/KynanUserbot?start=help"), Button.url("ᴅᴏɴᴀsɪ ​❤️", "https://graph.org/file/2982a27fe0e1500bf5b17.jpg")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
