import random
from pyrogram import Client, filters

# Emojis to randomly react with
EMOJIS = ["🤝", "😇", "🤗", "😍"]

@Client.on_message(filters.incoming & ~filters.service)
async def auto_react(client, message):
    try:
        # Only react to messages from real human users
        if not message.from_user or message.from_user.is_bot:
            return

        # Skip channels entirely
        if message.chat.type == "channel":
            return

        # React only if the Pyrogram version supports it
        if callable(getattr(message, "react", None)):
            await message.react(random.choice(EMOJIS))

    except Exception as e:
        print(f"[AutoReact Error] {e}")
