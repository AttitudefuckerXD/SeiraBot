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
  LUNA = "**Hella I'm ð³á´á´ ÉªÊâð°É³É ÉÆ!** \n\n"
  LUNA += "ð **I'm Working Properly** \n\n"
  LUNA += "ð **My Master : [Vijayâ](https://t.me/Attitude_king_vj)** \n\n"
  LUNA += f"ð **Telethon Version : {tlhver}** \n\n"
  LUNA += f"ð **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thanks for add me here ð**"
  BUTTON = [[Button.url("Êá´Êá´", "https://t.me/DevilxAngeLBot?start=help"), Button.url("sá´á´á´á´Êá´", "https://t.me/tgcalls_Musicxchat")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

