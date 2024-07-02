from loader import bot
from data.config import ADMINS

async def start_up():
    for i in ADMINS:
        await bot.send_message(chat_id=i, text="Bot ishga tushdi🟢")

async def shut_down():
    for i in ADMINS:
        await bot.send_message(chat_id=i, text="Bot to`xtadi🔴")