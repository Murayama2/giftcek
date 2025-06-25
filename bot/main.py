import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.user_handler import user_router
from handlers.user_handler import gift_router
from handlers.user_input_handler import register_user_handlers
from utils.gift_utils import gift_monitor

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # channel ID or user ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(gift_router)
    dp.include_router(user_router)

# Register user input handler
register_user_handlers(dp)

async def main():
    print("Bot started...")

    # Run gift monitoring in background
    asyncio.create_task(gift_monitor(bot, CHAT_ID))

    # Start polling user messages
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
