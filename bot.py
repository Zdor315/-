from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Обробник команди /start
async def start(update: Update, context) -> None:
    await update.message.reply_text("Привіт! Надішли мені повідомлення, і я повторю його.")

# Обробник звичайних повідомлень
async def echo(update: Update, context) -> None:
    user_message = update.message.text
    await update.message.reply_text(f"Ти написав: {user_message}")

# Основна функція запуску бота
def main():
    TOKEN = "7302913383:AAH8wW_QgxgBy4Ur7CWeiz6pOm_GJ3hOoEA"  # Замініть на токен вашого бота

    # Створення додатку
    app = ApplicationBuilder().token(TOKEN).build()

    # Додаємо обробники
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаємо бота
    print("Бот запущено. Натисніть Ctrl+C для зупинки.")
    app.run_polling()

if __name__ == "__main__":
    main()
