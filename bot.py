from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ---------------- CONFIG ----------------
BOT_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot token
PDFS = {
    "Physics Module": "AgAD1RMAApf-MVI",  # Replace or add your PDFs
    # "Math Notes": "BQACAgQAAxkBAAIB...",
    # "ICT Basics": "BQACAgQAAxkBAAIC..."
}
# ---------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for name in PDFS:
        keyboard.append([InlineKeyboardButton(name, callback_data=name)])
    await update.message.reply_text(
        "Welcome! Choose a PDF to receive:", 
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    file_id = PDFS.get(query.data)
    if file_id:
        await query.message.chat.send_document(file_id)
    else:
        await query.message.reply_text("PDF not found.")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to see the list of PDFs.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()