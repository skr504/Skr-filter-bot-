from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("info") & filters.private)
async def info_handler(client, message: Message):
    bot_user = await client.get_me()

    text = f"""🤖 **Bot Information**

**Name:** {bot_user.first_name}
**Username:** @{bot_user.username}
**ID:** `{bot_user.id}`
**Language:** Python (Pyrogram)
**Status:** Running ✅

📣 **Powered by** [@SKR_updates](https://t.me/SKR_updates)
"""
    await message.reply_text(text, disable_web_page_preview=True)
