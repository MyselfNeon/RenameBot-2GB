from pyrogram import Client, filters 
from helper.database import jishubotz

@Client.on_message(filters.private & filters.command(['set_caption', "sc"]))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Cᴀᴘᴛɪᴏɴ\n\nExᴀᴍᴘʟᴇ :- `/set_caption 📕 Nᴀᴍᴇ ➠ : {filename} \n\n🔗 Sɪᴢᴇ ➠ : {filesize} \n\n⏰ Dᴜʀᴀᴛɪᴏɴ ➠ : {duration}`__**")
    caption = message.text.split(" ", 1)[1]
    await jishubotz.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**__Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Aᴅᴅᴇᴅ__ ✅**")
   
@Client.on_message(filters.private & filters.command(['del_caption', "dc"]))
async def delete_caption(client, message):
    caption = await jishubotz.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**__Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ__ ❌**")
    await jishubotz.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**__Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ__ 🗑️**")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption', "vc"]))
async def see_caption(client, message):
    caption = await jishubotz.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**__Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ :__**\n\n`{caption}`")
    else:
       await message.reply_text("**__Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ ❌__**")









