# import os
# import logging
# import requests
# from aiohttp import ClientSession
# from dotenv import load_dotenv
# from telegram import Update, Bot
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# # Load environment variables
# load_dotenv()
# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# YANDEX_OAUTH_TOKEN = os.getenv("YANDEX_OAUTH_TOKEN")
# YANDEX_FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")
# YANDEX_GPT_API_ENDPOINT = os.getenv("YANDEX_GPT_API_ENDPOINT")

# # Enable logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# async def get_yandex_token(session):
#     url = YANDEX_GPT_API_ENDPOINT
#     headers = {
#         "Content-Type": "application/json",
#     }
#     data = {
#         "yandexPassportOauthToken": YANDEX_OAUTH_TOKEN
#     }
#     async with session.post(url, json=data, headers=headers) as response:
#         response_data = await response.json()
#         return response_data["iamToken"]

# async def get_gpt_response(session, iam_token, question):
#     url = f"https://iot-devices.api.cloud.yandex.net/v1/tts:synthesize"
#     headers = {
#         "Authorization": f"Bearer {iam_token}",
#         "Content-Type": "application/json",
#     }
#     data = {
#         "folderId": YANDEX_FOLDER_ID,
#         "text": question,
#         "lang": "ru-RU"
#     }
#     async with session.post(url, json=data, headers=headers) as response:
#         response_data = await response.json()
#         return response_data.get("response")

# async def handle_message(update: Update, context: CallbackContext):
#     question = update.message.text
#     async with ClientSession() as session:
#         iam_token = await get_yandex_token(session)
#         response = await get_gpt_response(session, iam_token, question)
#         update.message.reply_text(response)

# def start(update: Update, context: CallbackContext):
#     update.message.reply_text('Привет! Задайте мне вопрос, и я постараюсь ответить.')

# def main():
#     updater = Updater(TELEGRAM_TOKEN)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Токен вашего бота
TOKEN = '6771527857:AAHGz1g2vYk9rV4q1kbSadX80yu0eKNOLSA'

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот для ответов на вопросы. Отправьте мне свой вопрос.')

# Функция для обработки текстовых сообщений
def reply_message(update, context):
    question = update.message.text
    # Пример логики ответа на вопросы
    if 'погода' in question.lower():
        response = 'Сегодня отличная погода!'
    elif 'что такое' in question.lower():
        response = 'Это нечто важное!'
    else:
        response = 'Я не знаю, как на это ответить. Попробуйте спросить что-то другое.'

    update.message.reply_text(response)

def main():
    # Создаем экземпляр класса Updater
    updater = Updater(TOKEN, use_context=True)

    # Получаем объект Dispatcher для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчики текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
