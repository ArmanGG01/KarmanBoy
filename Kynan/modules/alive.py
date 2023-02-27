import os
import re
from platform import python_version as y
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Kynan.events import register
from Kynan import telethn as tbot


PHOTO = "https://telegra.ph/file/3f4c55755b365077bfc05.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"┏━━━━━━━━━━━━━━━━━━━━┓\n"
  TEXT += f"┠➣ **ᴋᴀʀᴍᴀɴ ʀᴏʙᴏᴛ** \n"
  TEXT += f"┠➣ **ᴍʏ ᴏᴡɴᴇʀ : [𝙰𝚁𝙼𝙰𝙽](https://t.me/PakkPoll)**\n"
  TEXT += f"┠➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`\n"
  TEXT += f"┠➣ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
  TEXT += f"┠➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"┠➣ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n"
  TEXT += "┗━━━━━━━━━━━━━━━━━━━━┛"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/KarmanMusicBot?start=help"), Button.url("ᴅᴏɴᴀsɪ ​❤️", "https://graph.org/file/2982a27fe0e1500bf5b17.jpg")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
