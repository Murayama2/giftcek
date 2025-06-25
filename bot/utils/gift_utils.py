import aiohttp
from aiogram import Bot

TONNEL_API_URL = "https://gifts3.tonnel.network/api/pageGifts"

# Ambil data gift terbaru dari API Tonnel
async def fetch_gifts():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(TONNEL_API_URL) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("data", [])
                else:
                    print(f"Failed to fetch gifts. Status code: {response.status}")
    except Exception as e:
        print(f"Error while fetching gifts: {e}")
    return []

# Kirim alert tentang gift ke chat
async def send_gift_alert(bot: Bot, chat_id, gift):
    title = gift.get("title", "New Gift")
    url = gift.get("url", "https://tonnel.io")
    image = gift.get("image")
    price = gift.get("price", 0)
    limit = gift.get("limit", "?")
    used = gift.get("used", 0)
    upgradeable = gift.get("upgradableToNft", False)

    caption = f"🎁 <b>{title}</b>\n"
    caption += f"💰 Price: {price} TON\n"
    caption += f"📦 Usage: {used}/{limit}\n"
    caption += f"✨ Upgradeable: {'Yes' if upgradeable else 'No'}\n"
    caption += f"\n🔗 <a href='{url}'>Claim Here</a>"

    try:
        if image:
            await bot.send_photo(chat_id, photo=image, caption=caption, parse_mode="HTML")
        else:
            await bot.send_message(chat_id, text=caption, parse_mode="HTML")
    except Exception as e:
        print(f"Failed to send message: {e}")
