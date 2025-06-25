import re
from aiogram import Router, F
from aiogram.types import Message
from utils.gift_utils import send_gift_alert, fetch_gifts

user_router = Router()

@user_router.message(F.text)
async def handle_nft_link(message: Message):
    print("📩 Menerima pesan:", message.text)

    match = re.search(r"https://t\.me/nft/([\w\-]+)", message.text.strip())
    if not match:
        return

    slug = match.group(1)
    print("🔍 Slug ditemukan:", slug)
    
    gifts = await fetch_gifts()
    for gift in gifts:
        if gift.get("slug") == slug:
            print("✅ Gift cocok, mengirim...")
            await send_gift_alert(message.bot, message.chat.id, gift)
            return

    await message.reply("❌ Gift not found or no longer available.")
