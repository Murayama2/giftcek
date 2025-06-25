from aiogram import types, Dispatcher
import re

nft_link_pattern = re.compile(r"https://t\.me/nft/([a-zA-Z0-9\-]+)")

async def handle_nft_link(message: types.Message):
    match = nft_link_pattern.search(message.text)
    if match:
        nft_id = match.group(1)
        nft_url = f"https://tonnel.io/nft/{nft_id}"
        await message.answer(f"🔍 Here is your NFT:\n{nft_url}")
    else:
        await message.answer("❌ Please send a valid NFT link like https://t.me/nft/JesterHat-1234")

def register_user_handlers(dp: Dispatcher):
    dp.message.register(handle_nft_link)￼Enter
