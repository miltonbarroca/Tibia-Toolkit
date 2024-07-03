import asyncio
import telegram #pip3 install python-telegram-bot
from conf import Constants

bot = telegram.Bot(token=Constants.TOKEN)

async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def send_photo(photo, chat_id):
    async with bot:
        await bot.send_photo(photo=photo, chat_id=chat_id)
