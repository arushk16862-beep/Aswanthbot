from pyrogram import Client, filters 
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command('set_start'))
async def set_start_message(c: Client, message):
    if len(message.text.split()) > 1:
        custom_text = message.text.html.split(None, 1)[1]
        await message.reply_text("Yᴏᴜʀ Sᴛᴀʀᴛ Mᴇssᴀɢᴇ Sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ")
    else:
        await message.reply_text("Please provide a text after command. Example: `/set_start Hello`")

