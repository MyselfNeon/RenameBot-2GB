from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config
from helper.database import jishubotz

async def not_subscribed(_, client, message):
    await jishubotz.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True

@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[InlineKeyboardButton(text="📢 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Config.FORCE_SUB}") ]]
    text = f"""<b><i>Hᴇʟʟᴏ {message.from_user.mention} \n\nYᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ \n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟ</i></b>"""
    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="**__Sᴏʀʀʏ Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Tᴏ Usᴇ Mᴇ__**")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text,quote=True, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text,quote=True, reply_markup=InlineKeyboardMarkup(buttons))


