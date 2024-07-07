from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Токен вашего бота
TOKEN = '6771527857:AAHGz1g2vYk9rV4q1kbSadX80yu0eKNOLSA'

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Привет! Я бот для ответов на вопросы. Отправьте мне свой вопрос.')

# Функция для обработки текстовых сообщений
async def reply_message(update: Update, context: CallbackContext):
    question = update.message.text
    # Пример логики ответа на вопросы
    if 'погода' in question.lower():
        response = 'Сегодня отличная погода!'
    elif 'что такое' in question.lower():
        response = 'Это нечто важное!'
    else:
        response = 'Я не знаю, как на это ответить. Попробуйте спросить что-то другое.'

    await update.message.reply_text(response)

def main():
    # Создаем экземпляр класса Application
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))

    # Регистрируем обработчики текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    main()
