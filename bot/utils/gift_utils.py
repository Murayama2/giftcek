import aiohttp
import json
from aiogram import Bot
import asyncio

TONNEL_API_URL = "https://gifts3.tonnel.network/api/pageGifts"

sent_gifts = set()

# Ambil data gift terbaru dari API Tonnel
async def fetch_gifts():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://market.tonnel.network",
        "Origin": "https://market.tonnel.network",
    }

    params = {
        "filter": json.dumps({}),
        "page": 1,
        "limit": 50
    }

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            print("📡 Fetching gifts with params:", params)
            print("📎 Headers:", headers)

            async with session.get(TONNEL_API_URL, params=params) as response:
                print("🔗 Final URL:", str(response.url))

                if response.status == 200:
                    data = await response.json()
                    return data.get("data", [])
                else:
                    print(f"❌ Failed to fetch gifts. Status code: {response.status}")
                    try:
                        print("💬 Response text:", await response.text())
                    except:
                        pass
    except Exception as e:
        print(f"⚠️ Error while fetching gifts: {e}")
    return []

# Kirim notifikasi gift ke Telegram
async def send_gift_alert(bot: Bot, chat_id, gift):
    title = gift.get("title", "New Gift")
    url = gift.get("url", "https://market.tonnel.network/")
    image = gift.get("image")
    price = gift.get("price", 0)
    limit = gift.get("limit", "?")
    used = gift.get("used", 0)
    upgradeable = gift.get("upgradableToNft", False)

    caption = (
        f"🎁 <b>{title}</b>\n"
        f"💰 Price: {price} TON\n"
        f"📦 Usage: {used}/{limit}\n"
        f"✨ Upgradeable: {'Yes' if upgradeable else 'No'}\n"
        f"\n🔗 <a href='{url}'>Claim Here</a>"
    )

    try:
        if image:
            await bot.send_photo(chat_id, photo=image, caption=caption, parse_mode="HTML")
        else:
            await bot.send_message(chat_id, text=caption, parse_mode="HTML")
        print(f"✅ Sent gift alert: {title}")
    except Exception as e:
        print(f"❌ Failed to send message: {e}")

# Loop pemantauan gift baru
async def gift_monitor(bot: Bot, chat_id):
    while True:
        gifts = await fetch_gifts()
        for gift in gifts:
            slug = gift.get("slug")
            if slug and slug not in sent_gifts:
                print(f"🔔 Gift baru ditemukan: {slug}")
                await send_gift_alert(bot, chat_id, gift)
                sent_gifts.add(slug)
        await asyncio.sleep(5)
