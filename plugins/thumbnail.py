from pyrogram import Client, filters 
from helper.database import jishubotz


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await jishubotz.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("<b><i>You Don't Have Any Thumbnail ❌</i></b>") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await jishubotz.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("<b><i>Thumbnail Deleted Successfully 🗑️</i></b>")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("<b><i>Please Wait ...</i></b>")
    await jishubotz.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("<i><b>Thumbnail Saved Successfully ✅️</b></i>")






