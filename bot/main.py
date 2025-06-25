import os
import time
import requests
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

# Store gift IDs to avoid duplicates
seen_gift_ids = set()

def get_latest_gifts(limit=10, offset=0):
    url = "https://gifts3.tonnel.network/api/pageGifts"
    payload = {
        "offset": offset,
        "limit": limit,
        "sortBy": "newest"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data.get("gifts", [])

def send_gift_alert(gift):
    title = gift.get("title", "Gift Baru")
    price = gift.get("price", 0)
    limit = gift.get("limit", "?")
    used = gift.get("used", 0)
    upgradeable = gift.get("upgradableToNft", False)
    image = gift.get("image", None)
    url = gift.get("url", "https://tonnel.io")

    message = (
        f"🎁 <b>Gift Baru Tersedia!</b>\n\n"
        f"🧩 <b>{title}</b>\n"
        f"💰 Harga: {price} ⭐\n"
        f"📦 Limit: {used}/{limit}\n"
        f"🪄 Upgradeable: {'✅ Ya' if upgradeable else '❌ Tidak'}\n"
        f"🔗 <a href=\"{url}\">Lihat Gift</a>"
    )

    bot.send_photo(chat_id=CHAT_ID, photo=image, caption=message, parse_mode='HTML')

# Main loop
if __name__ == '__main__':
    print("🤖 Bot sedang berjalan...")
    while True:
        try:
            gifts = get_latest_gifts()
            for gift in gifts:
                gift_id = gift.get("id")
                if gift_id not in seen_gift_ids:
                    send_gift_alert(gift)
                    seen_gift_ids.add(gift_id)

            time.sleep(60)

        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)
