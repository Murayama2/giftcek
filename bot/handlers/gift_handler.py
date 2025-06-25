import asyncio
import aiohttp
from utils.gift_utils import send_gift_alert

TONNEL_API_URL = "https://gifts3.tonnel.network/api/pageGifts"

seen_gift_ids = set()

async def fetch_gifts():
    async with aiohttp.ClientSession() as session:
        async with session.get(TONNEL_API_URL) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("gifts", [])
            return []

async def gift_monitor(bot, chat_id):
    global seen_gift_ids
    while True:
        try:
            gifts = await fetch_gifts()
            for gift in gifts:
                gift_id = gift.get("id")
                if gift_id and gift_id not in seen_gift_ids:
                    seen_gift_ids.add(gift_id)
                    await send_gift_alert(bot, chat_id, gift)
        except Exception as e:
            print(f"Error in gift monitor: {e}")
        await asyncio.sleep(5)
