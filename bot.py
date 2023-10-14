import telebot
from flask import Flask, request
import os
from src.setup import MODE, API_TOKEN, bot, logger
from src.accepted_commands import accepted_commands, handlers
from src.messages import random_ignore_mudoc
import logging #you know for logging purpose

if MODE == "prod":
    def run():
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
else:
    def run():
        bot.polling()

server = Flask(__name__)


@bot.message_handler(commands=accepted_commands)
def general_handler(message):
    try:
        key = message.text.replace(
            '/', '').replace('@infoUNO_bot', '').replace('@UNOTestBots_BOT', '').split(' ')
        if(message.from_user.id == 710345708):
            bot.send_message(message.chat.id, random_ignore_mudoc())
        handlers[key[0]](message)
    except Exception as e:
        logging.error(f"Error en general_handler: {e}")


@bot.message_handler(content_types=["new_chat_members"])
def welcome_new_members(message):
    try:
        handlers['welcome'](message)
    except Exception as e:
        logging.error(f"Error en welcome_new_members: {e}")


@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    try:
        bot.process_new_updates(
            [telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    except Exception as e:
        logging.error(f"Error al procesar actualizaciones: {e}")
    return "!", 200


@server.route("/")
def webhook():
    try:
        bot.remove_webhook()
        bot.set_webhook(url=os.environ.get('URL_NAME') + API_TOKEN)
    except Exception as e:
        logging.error(f"Error en webhook: {e}")
    return "!", 200


if __name__ == "__main__":
    run()
