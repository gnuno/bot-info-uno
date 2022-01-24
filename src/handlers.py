from src.setup import bot, logger
from src.helpers import get_links_message, get_info, get_links_from_api, url_message, url_correlatives
import src.messages as responses


def welcome_new_user(message):
    is_bot = message.json['new_chat_participant']['is_bot']
    if not is_bot:
        new_user_id = message.json['new_chat_participant']['id']
        logger.info(
            f"El usuario {new_user_id} se ha unido al grupo.")
        chat_id = message.chat.id
        username = message.json['new_chat_participant']['username']
        bot.send_message(
            chat_id, f"Bienvenidx @{username}. Recordá leer las reglas y que con el comando <b>/help</b> puedo ayudarte.")


def send_welcome(message):
    bot.reply_to(
        message, "Bienvenidx a este botardo con información util sobre la Universidad Nacional del Oeste. Escribí <b>/help</b> para saber cómo seguir.")


def help_message(message):
    user_id = message.from_user.id
    logger.info(f"El usuario {user_id} ha solicitado AYUDA.")
    chat_id = message.chat.id
    bot.send_message(chat_id, responses.help_message())


def get_useful_links(message):
    user_id = message.from_user.id
    logger.info(f"El usuario {user_id} ha solicitado LINKS.")
    chat_id = message.chat.id
    bot.send_message(chat_id, get_links_message())


def request_url_information(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(
        f"El usuario {user_id} ha solicitado información de {message.text}.")
    if message.text == "/siu":
        url = 'https://autogestion.uno.edu.ar/uno/'
        name = "siu guarani"
    elif message.text == "/campus":
        url = 'http://campusvirtual.uno.edu.ar/moodle/'
        name = 'campus'

    bot.send_message(
        chat_id, f"<i>Solicitando información a {url} ...</i>")
    bot.send_message(chat_id, url_message(url, name))


def get_comunidades_it(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(f"El usuario {user_id} ha solicitado Comunidades IT.")
    bot.send_message(chat_id, responses.comunidades_it())


def get_academic_calendar(message):
    arguments = message.text.split()
    user_id = message.from_user.id
    chat_id = message.chat.id
    if len(arguments) > 1 and arguments[1] == 'feriados':
        logger.info(
            f"El usuario {user_id} ha solicitado el Calendario de Feriados.")
        bot.send_message(chat_id, responses.calendario_feriados_message())
    else:
        logger.info(
            f"El usuario {user_id} ha solicitado el Calendario Académico.")
        bot.send_message(chat_id, responses.calendario_academico_message())


def get_emails(message):
    arguments = message.text.split()
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.info(f"El usuario {user_id} ha solicitado MAILS.")
    if len(arguments) > 1:
        bot.send_message(chat_id, responses.get_mails_by_term(arguments[1]))
    else:
        bot.send_message(chat_id, responses.get_mails_by_term())


def send_curriculum(message):
    chat_id = message.chat.id
    message_id = message.message_id
    doc = open('./assets/curriculum/plan-de-estudios-inf.png', 'rb')
    bot.send_photo(chat_id, doc, reply_to_message_id=message_id)

def get_correlatives(message):
    args = message.text.split()
    args.pop(0)
    materia = ' '.join(args)
    logger.info(f"El usuario {message.from_user.id} ha solicitado CORRELATIVAS de {materia}.")

    if len(args) == 0:
        bot.send_message(message.chat.id, "Para conocer las correlativas de una materia usa este comando junto a el nombre de la materia a solicitar.\n Ejemplo: /correlative analisis matematico ii")
    else:
        bot.send_message(message.chat.id, url_correlatives(materia))