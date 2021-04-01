import telebot
from flask import Flask, request
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenido a este bot de prueba")


@bot.message_handler(commands=['siu'])
def send_welcome(message):
    user_id = message['from_user']['id']
    logger.info(f"El usuario {user_id} ha solicitado información sobre el SIU")
    bot.reply_to(message, "Comando SIU")


@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get('URL_NAME') + API_TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
