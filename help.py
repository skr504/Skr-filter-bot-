from pyrogram import Client, filters

@Client.on_message(filters.command("help") & filters.private)
async def help_handler(client, message):
    await message.reply_text(
        text=(
            "**🛠 Help Menu**\n\n"
            "/start - Welcome message\n"
            "/info - Show bot info\n"
            "/help - Show this help message\n"
            "/status - Admin-only status\n\n"
            "📂 This bot can auto-filter files from connected channels.\n"
            "💾 Supports MongoDB storage and forwarding.\n\n"
            "🔗 Powered by @SKR_updates"
        )
    )
