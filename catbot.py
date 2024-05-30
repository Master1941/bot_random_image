import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from log_execution import log_execution, logging

load_dotenv()


token = os.getenv("TELEGRAM_TOKEN")
URL = os.getenv("URL", "https://api.thecatapi.com/v1/images/search")


@log_execution
def get_new_image():
    """Делать запросы к thecatapi.com."""
    try:
        response = requests.get(URL)
    except Exception:
        logging.exception("Ошибка при запросе к основному API")
        # присылает фото собачки
        new_url = "https://api.thedogapi.com/v1/images/search"
        response = requests.get(new_url)
    response = response.json()
    random_cat = response[0].get("url")
    return random_cat


@log_execution
def new_cat(update, context):
    """На запрос /newcat отправляет новую картинку с котиком."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


@log_execution
def wake_up(update, context):
    """На запрос /start отправляет картинку с котиком."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup(
        [["/newcat"]],
        resize_keyboard=True,
    )
    context.bot.send_message(
        chat_id=chat.id,
        text=f"Привет, {name}. Посмотри какого котика я тебе нашел",
        reply_markup=button,
    )
    context.bot.send_photo(chat.id, get_new_image())


@log_execution
def say_hi(update, context):
    """На любое сообщение отправляет приветствие."""
    chat = update.effective_chat
    button = ReplyKeyboardMarkup(
        [["/start"]],
        resize_keyboard=True,
    )
    context.bot.send_message(
        chat_id=chat.id,
        text="Привет, я KittyBot!",
        reply_markup=button,
    )


@log_execution
def main():
    """главная функция."""
    updater = Updater(token)
    updater.start_polling(poll_interval=11.0)
    updater.dispatcher.add_handler(CommandHandler("start", wake_up))
    updater.dispatcher.add_handler(CommandHandler("newcat", new_cat))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
