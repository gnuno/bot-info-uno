import telebot
from flask import Flask, request
import os
from src.setup import MODE, API_TOKEN, bot, logger
from src.accepted_commands import accepted_commands, handlers

if MODE == "prod":
    def run():
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
else:
    def run():
        bot.polling()

server = Flask(__name__)


@bot.message_handler(commands=accepted_commands)
def general_handler(message):
    handlers[message.text.replace('/', '')](message)


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
    run()
