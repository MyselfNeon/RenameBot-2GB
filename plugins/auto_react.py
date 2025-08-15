import random
from pyrogram import Client, filters

# Emojis to randomly react with
EMOJIS = ["🤝", "😇", "🤗", "😍"]

@Client.on_message(filters.incoming & ~filters.service)
async def auto_react(client, message):
    try:
        # Avoid reacting to our own bot's messages
        if message.from_user and message.from_user.is_self:
            return

        # Only react if 'react' method exists in this Pyrogram version
        if callable(getattr(message, "react", None)):
            await message.react(random.choice(EMOJIS))

    except Exception as e:
        # Print error in logs but never crash the bot
        print(f"[AutoReact Error] {e}")
