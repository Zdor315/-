from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функція обробки команди /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привіт! Я твій простий Telegram-бот. Напиши мені щось!")

# Функція обробки звичайних повідомлень
def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    update.message.reply_text(f"Ти написав: {user_message}")

# Основна функція
def main():
    # Встав свій токен сюди
    TOKEN = "7302913383:AAH8wW_QgxgBy4Ur7CWeiz6pOm_GJ3hOoEA"

    # Ініціалізуємо Updater
    updater = Updater(TOKEN)

    # Додаємо обробники для команд і повідомлень
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаємо бота
    updater.start_polling()
    print("Бот запущено. Натисни Ctrl+C для зупинки.")
    updater.idle()

if __name__ == "__main__":
    main()

