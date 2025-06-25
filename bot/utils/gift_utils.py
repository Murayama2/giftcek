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
            # Debug
            print("📡 Fetching gifts with params:", params)
            print("📎 Headers:", headers)
            req = session.get(TONNEL_API_URL, params=params)
            print("🔗 Final URL:", str(req.url))

            async with req as response:
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
