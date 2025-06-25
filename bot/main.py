import os
import time
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from bot.utils.fetch import fetch_new_gifts
from bot.utils.format import format_gift_message

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=BOT_TOKEN)

seen_ids = set()

if __name__ == '__main__':
    print("🚀 Bot is running...")
    while True:
        try:
            gifts = fetch_new_gifts()
            for gift in gifts:
                gift_id = gift.get("id")
                if gift_id and gift_id not in seen_ids:
                    seen_ids.add(gift_id)
                    text, image_url, buttons = format_gift_message(gift)
                    if image_url:
                        bot.send_photo(chat_id=CHAT_ID, photo=image_url, caption=text, parse_mode="HTML", reply_markup=buttons)
                    else:
                        bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="HTML", reply_markup=buttons)
            time.sleep(60)
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)