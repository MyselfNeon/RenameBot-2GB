import random
from pyrogram import Client, filters

EMOJIS = ["🤝"]

@Client.on_message(filters.incoming & ~filters.service)
async def auto_react(client, message):
    try:
        # Safety: skip if no user or if user is a bot (including our own bot)
        if not message.from_user or message.from_user.is_bot:
            return

        # Safety: skip if chat is a channel
        if message.chat.type == "channel":
            return

        try:
            emoji = random.choice(EMOJIS)
        except Exception as e:
            print(f"[AutoReact] Emoji selection failed: {e}")
            return

        try:
            if callable(getattr(message, "react", None)):
                await message.react(emoji)
        except Exception as e:
            print(f"[AutoReact] Reaction failed: {e}")

    except Exception as e:
        print(f"[AutoReact] General error: {e}")
