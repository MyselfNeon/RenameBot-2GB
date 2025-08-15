import random
from pyrogram import Client, filters

# List of emojis to randomly choose from
EMOJIS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏"]

@Client.on_message(filters.incoming & ~filters.service)
async def auto_react(client, message):
    try:
        # Pick a random emoji from the list
        emoji = random.choice(EMOJIS)
        await message.react(emoji)
    except Exception as e:
        print(f"[AutoReact] Reaction failed: {e}")

  
