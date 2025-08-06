import os
import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from helper.progress import progress_for_pyrogram
from helper.database import jishubotz
from helper.ffmpeg import set_custom_metadata

@Client.on_message(filters.document | filters.video | filters.audio)
async def rename_file(bot, message: Message):
    try:
        file = message.document or message.video or message.audio
        file_name = file.file_name
        file_size = file.file_size

        await message.reply_text("📥 Downloading...")

        download_location = f"downloads/{file.file_unique_id}_{file_name}"
        start_time = time.time()

        downloaded_file_path = await bot.download_media(
            message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=("⬇️ Downloading", message, start_time)
        )

        await message.reply_text("✏️ Renaming...")

        # Get custom name from user DB (if set)
        custom_name = await jishubotz.get_custom_rename(message.from_user.id)
        if custom_name:
            ext = os.path.splitext(file_name)[1]
            new_file_name = f"{custom_name}{ext}"
        else:
            new_file_name = file_name

        new_download_location = f"downloads/{file.file_unique_id}_{new_file_name}"
        os.rename(downloaded_file_path, new_download_location)

        await message.reply_text("🧪 Embedding Metadata...")

        # Get user custom metadata
        user_meta = await jishubotz.get_metadata_code(message.from_user.id)

        # Define new path with metadata
        ext = os.path.splitext(new_download_location)[1]
        new_path = new_download_location.replace(ext, f"_meta{ext}")

        # Apply ffmpeg metadata
        final_file = await set_custom_metadata(new_download_location, new_path, user_meta)

        await message.reply_text("📤 Uploading...")

        # Send final file with metadata
        await message.reply_document(
            document=final_file,
            caption=f"✅ File processed with embedded metadata:\n`{user_meta}`"
        )

        # Clean up
        try:
            os.remove(new_download_location)
            os.remove(final_file)
        except:
            pass

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")
