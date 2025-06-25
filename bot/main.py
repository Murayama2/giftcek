import asyncio
import logging
import os
from aiogram import Bot

from handlers.gift_handler import gift_monitor

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

async def main():
    await gift_monitor(bot, CHAT_ID)

if __name__ == "__main__":
    asyncio.run(main())
