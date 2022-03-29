import json
import requests
import random 
from unidecode import unidecode
from datetime import datetime
LINKS_ROOT_URL = 'https://gea-uno.github.io/'
API_URL = 'https://gealinks-api.herokuapp.com/'


def url_success_message(latency, name):
    return f"El {name} ha respondido <b>exitosamente</b> con una latencia de <b>{latency}ms</b>"


def url_failure_message(name):
    return f"<b>Falló</b> la solicitud al {name}. Al parecer está caído."


def help_message():
    with open('./assets/messages/help.txt', encoding='utf-8') as f:
        message = f.read()

    return message


def links_message(data):
    message = f"Links utiles de la UNO en general:\n\n"
    for name in data:
        if name == 'info':
            info = f"<b>Informática</b>: {LINKS_ROOT_URL}{name}\n"
        elif name == 'enf':
            enf = f"<b>Enfermería</b>: {LINKS_ROOT_URL}{name}\n"
        elif name == 'admin':
            admin = f"<b>Administración</b>: {LINKS_ROOT_URL}{name}\n"
        elif name == 'hum':
            hum = f"<b>Humanidades</b>: {LINKS_ROOT_URL}{name}\n"
        elif name == 'ingq':
            ingq = f"<b>Ing. Química</b>: {LINKS_ROOT_URL}{name}\n"
        elif name == 'links':
            links = f"<b>Plataformas UNO</b>: {LINKS_ROOT_URL}uno\n"
        elif name == 'info-comun':
            comunidades = f"<b>Comunidades IT</b>: /comunidades_it\n"

    message = message + info + comunidades + enf + admin + hum + ingq + links
    message += f"\nY acá te dejamos el dashboard principal por si querés chusmear desde cero!\n{LINKS_ROOT_URL}"
    return message


def calendario_academico_message():
    with open('./assets/messages/calendario-academico.txt', encoding='utf-8') as f:
        message = f.read()
    return message


def calendario_feriados_message():
    with open('./assets/calendario_feriados.json', encoding="utf-8") as f:
        calendario = json.load(f)
    message = f"Calendario Feriados {datetime.today().year}:\n\n"
    for mes in calendario:
        message += f"<b><u>{mes['mes']}</u></b>\n"
        if not mes['feriados']:
            message += f"Ninguno\n"
        else:
            for feriado in mes['feriados']:
                message += f"<u>{feriado['dia']}:</u> {feriado['motivo']}\n"
    return message


def comunidades_it():
    url = f'{API_URL}link?father=/info/comunidades'
    comunidades = requests.get(url).json()['data']

    message = f"Las comunidades IT son: \n\n"

    for item in comunidades:
        message += f"<b><u>{item['title']}</u></b>: {item['url']}. \n"
    return message


def build_mails_message(array):
    message = ''
    for item in array:
        message += f"\n<u>Escuela de {item['escuela']}</u>\n"
        for mail in item['mails']:
            message += f"<b>{mail['name']}</b>: {mail['mail']}\n"
    return message


def get_mails_by_term(*term):
    message = f'Acá tenés los mails:\n'
    with open('./assets/mails_escuelas.json', encoding='utf-8') as f:
        mails = json.load(f)

    if len(term) > 0:
        result = filter(lambda x: unidecode(
            term[0]).lower() in unidecode(x['escuela']).lower(), mails)
        message += build_mails_message(list(result))
    else:
        message += build_mails_message(mails)

    return message

def random_ignore_mudoc():
    options = ["Shh", "Hoy no murd0c", "Otra vez vos?", "Te voy a acusar con mi mamá!", "ehh no se JAJAJA lpm"]
    return random.choice(options)