from pyrogram import Client, filters
from config import ADMINS

@Client.on_message(filters.command("status") & filters.private & filters.user(ADMINS))
async def status_handler(client, message):
    await message.reply_text("✅ Bot is up and running!\n\nAdmin access confirmed.")
