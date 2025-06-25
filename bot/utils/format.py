from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def format_gift_message(gift):
    title = gift.get("title", "New Gift")
    image = gift.get("image", "")
    stats = gift.get("stats", {})
    url = gift.get("url", "https://tonnel.io")

    floor = stats.get("floor", "?")
    avg = stats.get("avg", "?")
    last = stats.get("last", "?")
    history = stats.get("history", [])

    text = f"<b>{title}</b>\n"
    text += f"Floor: {floor} TON\n"
    text += f"AVG: {avg} TON\n"
    text += f"Last sale: {last} TON\n"
    if history:
        text += "\n<b>Sell history:</b>\n"
        for h in history[:5]:
            text += f"{h}\n"

    buttons = InlineKeyboardMarkup([[
        InlineKeyboardButton("🛒 View on Tonnel", url=url)
    ]])

    return text, image, buttons