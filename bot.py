import telebot
from flask import Flask, request
import os
import logging
import requests
import time
import messages as responses

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

MODE = os.environ.get("MODE")

if MODE == "prod":
    API_TOKEN = os.environ.get('TOKEN')
    bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML') 
    def run():
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
else :
    API_TOKEN = '1761269185:AAFrxdpg13lS4X6NaHnENizGKa0VXsW9z9c'
    bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')
    def run():
        bot.polling()

server = Flask(__name__)


def get_info(url):
    url_data = dict()
    t0 = time.time()
    r = requests.get(url)
    t1 = time.time()
    url_data['status'] = r.status_code
    url_data['latency'] = int((t1-t0) * 1000)
    return url_data


def get_links_from_api():
    res = requests.get('https://igna98.alwaysdata.net/page')
    data = res.json()['data']
    mapped_list = list(map(lambda link: link['name'], data))
    return responses.links_message(mapped_list)


def url_message(url, name):
    url_data = get_info(url)
    if url_data['status'] == 200:
        return responses.url_success_message(url_data['latency'], name)
    else:
        return responses.url_failure_message(url_data['latency'], name)


def get_links_message():
    return get_links_from_api()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "Bienvenidx a este botardo con información util sobre la Universidad Nacional del Oeste. Escribí <b>/help</b> para saber cómo seguir.")


@bot.message_handler(commands=['help'])
def help_message(message):
    user_id = message.from_user.id
    logger.info(f"El usuario {user_id} ha solicitado AYUDA.")
    chat_id = message.chat.id
    bot.send_message(chat_id, responses.help_message())


@bot.message_handler(commands=['links'])
def get_useful_links(message):
    user_id = message.from_user.id
    logger.info(f"El usuario {user_id} ha solicitado LINKS.")
    chat_id = message.chat.id
    bot.send_message(chat_id, get_links_message())


@bot.message_handler(commands=['siu', 'campus'])
def request_url_information(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(f"El usuario {user_id} ha solicitado información de {message.text}.")
    if message.text == "/siu":
        url = 'https://autogestion.uno.edu.ar/uno/'
        name = "siu guarani"
    elif message.text == "/campus":
        url = 'http://campusvirtual.uno.edu.ar/moodle/'
        name = 'campus'

    bot.send_message(
        chat_id, f"<i>Solicitando información a {url} ...</i>")
    bot.send_message(chat_id, url_message(url, name))


@bot.message_handler(commands=['calendar'])
def get_academic_calendar(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(f"El usuario {user_id} ha solicitado el Calendario Academico.")
    bot.send_message(chat_id, responses.calendario_academico_message())


@bot.message_handler(commands=['mails'])
def get_emails(message):
    arguments = message.text.split()
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(f"El usuario {user_id} ha solicitado MAILS.")
    if len(arguments) > 1:
        bot.send_message(chat_id, responses.get_mails_by_term(arguments[1]))
    else:
        bot.send_message(chat_id, responses.get_mails_by_term())


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
