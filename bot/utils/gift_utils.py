from aiogram.types import InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup

async def send_gift_alert(bot, chat_id, gift):
    title = gift.get("title", "New Gift")
    price = gift.get("price", 0)
    limit = gift.get("limit", "?")
    used = gift.get("used", 0)
    upgradeable = gift.get("upgradableToNft", False)
    image = gift.get("image", None)
    url = gift.get("url", "https://tonnel.io")

    caption = f"🎁 <b>{title}</b>\n"
    caption += f"💰 Price: {price} TON\n"
    caption += f"📦 Usage: {used}/{limit}\n"
    caption += f"✨ Upgradeable: {'Yes' if upgradeable else 'No'}"

    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔗 View Gift", url=url)]
    ])

    try:
        if image:
            await bot.send_photo(chat_id, photo=image, caption=caption, reply_markup=buttons, parse_mode="HTML")
        else:
            await bot.send_message(chat_id, caption, reply_markup=buttons, parse_mode="HTML")
    except Exception as e:
        print(f"Failed to send message: {e}")
