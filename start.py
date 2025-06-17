from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/5924d32cbdc949f7df047-64dc1f885fdbc5b102.jpg",
        caption="👋 Hello! I'm your Filter Bot.\n\nI can save filters, serve files, and more!\n\n📣 Powered by @SKR_updates"
    )
