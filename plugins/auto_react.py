import random
from pyrogram import Client, filters

# List of emojis to randomly choose from
EMOJIS = ["🤝", "😇", "🤗", "😍"]

@Client.on_message(filters.incoming & ~filters.service)
async def auto_react(client, message):
    try:
        # Check if 'react' method exists (Pyrogram 2.x+)
        if callable(getattr(message, "react", None)):
            emoji = random.choice(EMOJIS)
            await message.react(emoji)
    except Exception as e:
        # Print error without crashing bot
        print(f"[AutoReact Error] {e}")
