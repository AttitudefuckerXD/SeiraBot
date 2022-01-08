import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/a01ef91bd802109bbcbc1.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm 𝙳ᴇᴠɪʟ✗𝙰ɳɠɛƖ!** \n\n"
  LUNA += "💎 **I'm Working Properly** \n\n"
  LUNA += "💎 **My Master : [Vijay★](https://t.me/Attitude_king_vj)** \n\n"
  LUNA += f"💎 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"💎 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terima kasih sudah menambahkan 𝙳ᴇᴠɪʟ✗𝙰ɳɠɛƖ 💜**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/DevilxAngeLBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/seirasupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

