from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import jishubotz
from pyromod.exceptions import ListenerTimeout
from config import Txt

ON = [[InlineKeyboardButton('Metadata On ✅', callback_data='metadata_1')],
      [InlineKeyboardButton('Set Custom Metadata', callback_data='custom_metadata')]]

OFF = [[InlineKeyboardButton('Metadata Off ❌', callback_data='metadata_0')],
       [InlineKeyboardButton('Set Custom Metadata', callback_data='custom_metadata')]]


@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    ms = await message.reply_text("**Please Wait...**", reply_to_message_id=message.id)
    bool_metadata = await jishubotz.get_metadata(message.from_user.id)
    user_metadata = await jishubotz.get_metadata_code(message.from_user.id)
    await ms.delete()

    reply_markup = InlineKeyboardMarkup(ON) if bool_metadata else InlineKeyboardMarkup(OFF)
    await message.reply_text(
        f"**Your Current Metadata :-**\n\n➜ `{user_metadata}` ",
        quote=True,
        reply_markup=reply_markup
    )


@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    data = query.data

    if data.startswith('metadata_'):
        _bool = data.split('_')[1]
        user_metadata = await jishubotz.get_metadata_code(query.from_user.id)

        if bool(eval(_bool)):
            await jishubotz.set_metadata(query.from_user.id, bool_meta=False)
            await query.message.edit(
                f"**Your Current Metadata :-**\n\n➜ `{user_metadata}` ",
                reply_markup=InlineKeyboardMarkup(OFF)
            )
        else:
            await jishubotz.set_metadata(query.from_user.id, bool_meta=True)
            await query.message.edit(
                f"**Your Current Metadata :-**\n\n➜ `{user_metadata}` ",
                reply_markup=InlineKeyboardMarkup(ON)
            )

    elif data == "custom_metadata":
        try:
            await query.message.delete()
            ask = await bot.ask(
                query.from_user.id,
                "**Send me your custom metadata string:**\n\n"
                "You can use variables like: `{filename}`, `{filesize}`, `{duration}` etc.",
                timeout=60
            )
            await jishubotz.set_metadata_code(query.from_user.id, ask.text)
            await bot.send_message(query.from_user.id, "✅ Metadata updated successfully!")

        except ListenerTimeout:
            await bot.send_message(query.from_user.id, "❌ Timeout! Please try again.")
