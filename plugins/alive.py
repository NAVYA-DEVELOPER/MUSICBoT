import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3f87af079e460935fb8fa.jpg",
        caption=f"""**I แดแด ๐๐๐ซ๐๐ ๐๐๐๐๐พ ๐ฝ๐๐
สแดแด สแดษดแดสแด สส [๐๐๐ซ๐ฎ๐](https://t.me/WTF_NAVYA)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " โฐ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญโฑ ", url=f"https://t.me/NavyaSupport")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "hi", "Navya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b45327792042629927c09.jpg",
        caption=f"""Hiโบ๏ธ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " โฐ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญโฑ ", url=f"https://t.me/TheNavya")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f01b866242fa4e3bf74ad.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " โฐ๐๐๐ฅ๐ค๐จ๐๐ฉ๐ค๐ง๐ฎโฑ ", url=f"https://t.me/TheNavya")
                ]
            ]
        ),
    )
