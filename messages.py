import json
from unidecode import unidecode
LINKS_ROOT_URL = 'https://gea-uno.github.io/'


def url_success_message(latency, name):
    return f"El {name} ha respondido <b>exitosamente</b> con una latencia de <b>{latency}ms</b>"


def url_failure_message(latency, name):
    return f"Falló la solicitud al {name} con una latencia de <b>{latency}ms</b>"


def help_message():
    message = f"<b>infoUNObot</b> te brinda información necesaria sobre la Universidad Nacional del Oeste, desde el estado del siu o el campus, hasta fechas importantes o links utiles.\n\n"
    message += f"<b>/help</b> - Muestra este mensaje.\n"
    message += f"<b>/siu</b> - Obtiene información del siu para saber el estado del mismo y su latencia.\n"
    message += f"<b>/links</b> - Te devuelve un listado de links utiles sobre la carrera (grupos, comunidades, etc).\n"
    message += f"<b>/calendar</b> - Te muestra las fechas importantes del calendario académico de la Universidad.\n"
    message += f"<b>/mails</b> - Te muestra los mails más importantes de las escuelas, además si especificás la escuela te filtra el resultado.\n"
    message += f"\nEste bot fue posible y llevado a cabo gracias a GNUno, cualquier consulta o pregunta hacela aquí: <i>https://t.me/gnuno_merlo</i>."
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
            comunidades = f"<b>Comunidades IT</b>: {LINKS_ROOT_URL}info/{name}\n"

    message = message + info + comunidades + enf + admin + hum + ingq + links
    message += f"\nY acá te dejamos el dashboard principal por si querés chusmear desde cero!\n{LINKS_ROOT_URL}"
    return message


def get_dates(dicc):
    message = ''
    if 'inscripcion' in dicc:
        message += f"Inscripcion: {dicc['inscripcion']}\n"
    if 'inicio' in dicc:
        message += f"Inicio: {dicc['inicio']}\n"
    if 'finalizacion' in dicc:
        message += f"Finalizacion: {dicc['finalizacion']}\n"
    if 'examenes' in dicc:
        message += f"Examanes: {dicc['examenes']}\n"
    return message


def calendario_academico_message():
    with open('./assets/calendario_academico.json', encoding='utf-8') as f:
        calendario = json.load(f)
    message = f"El calendario acádemico es el siguiente:\n\n"
    matches = ['Inscripción a Carreras de Grado', 'Exámenes Turno']
    for item in calendario:
        message += f"<b><u>{item['titulo']}</u></b>\n"
        para = item['actividades']['para']
        isMatch = [True for x in matches if x in item['titulo']]
        if 'regulares' in para:
            if True not in isMatch:
                message += f"<b>Regulares</b>\n"
            message += f"{get_dates(para['regulares'])}\n"
        if 'ingresantes' in para:
            if True not in isMatch:
                message += f"<b>Ingresantes</b>\n"
            message += f"{get_dates(para['ingresantes'])}\n"
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
