from pyrogram import Client, filters, enums
from helper.database import jishubotz


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Pʀᴇғɪx__\n\nExᴀᴍᴘʟᴇ - `/set_prefix @NeonFiles`**")
    prefix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**")
    await jishubotz.set_prefix(message.from_user.id, prefix)
    await JishuDeveloper.edit("**__Pʀᴇғɪx Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅__**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    JishuDeveloper = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**")
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if not prefix:
        return await JishuDeveloper.edit("**__Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇғɪx ❌__**")
    await jishubotz.set_prefix(message.from_user.id, None)
    await JishuDeveloper.edit("**__Pʀᴇғɪx Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ 🗑️__**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    JishuDeveloper = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**")
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if prefix:
        await JishuDeveloper.edit(f"**__Yᴏᴜʀ Pʀᴇғɪx__ -**\n\n`{prefix}`")
    else:
        await JishuDeveloper.edit("**__Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇғɪx ❌__**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Sᴜғғɪx__\n\nExample:- `/set_suffix @Madflix_Bots`**")
    suffix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**")
    await jishubotz.set_suffix(message.from_user.id, suffix)
    await JishuDeveloper.edit("**__Sᴜғғɪx Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅__**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    JishuDeveloper = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**")
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if not suffix:
        return await JishuDeveloper.edit("**__Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜғғɪx ❌__**")
    await jishubotz.set_suffix(message.from_user.id, None)
    await JishuDeveloper.edit("**__Sᴜғғɪx Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅__**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    JishuDeveloper = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**")
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if suffix:
        await JishuDeveloper.edit(f"**__Yᴏᴜʀ Sᴜғғɪx__ -**\n\n`{suffix}`")
    else:
        await JishuDeveloper.edit("**__Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜғғɪx ❌__**")








