import json
LINKS_ROOT_URL = 'https://gea-uno.github.io/'

with open('./assets/calendario_academico.json') as f:
    calendario = json.load(f)


def siu_success_message(latency):
    return f"El siu guaraní ha respondido <b>exitosamente</b> con una latencia de <b>{latency}ms</b>"


def siu_failure_message(latency):
    return f"Falló la solicitud al siu guaraní con una latencia de <b>{latency}ms</b>"


def help_message():
    return f"<b>infoUNObot</b> te brinda información necesaria sobre la Universidad Nacional del Oeste, desde el estado del siu o el campus, hasta fechas importantes o links utiles.\n\n<b>/help</b> - Muestra este mensaje.\n<b>/siu</b> - Obtiene información del siu para saber el estado del mismo y su latencia.\n<b>/links</b> - Te devuelve un listado de links utiles sobre la carrera (grupos, comunidades, etc).\n<b>/calendar</b> - Te muestra las fechas importantes del calendario académico de la Universidad.\n\nEste bot fue posible y llevado a cabo gracias a GNUno, cualquier consulta o pregunta hacela aquí: <i>inserte contacto de gnuno</i>."


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
    message = f"El calendario acádemico es el siguiente:\n\n"
    for item in calendario:
        message += f"<b><u>{item['titulo']}</u></b>\n"
        para = item['actividades']['para']
        if 'regulares' in para:
            message += f"<b>Regulares</b>\n"
            message += f"{get_dates(para['regulares'])}\n"
        if 'ingresantes' in para:
            message += f"<b>Ingresantes</b>\n"
            message += f"{get_dates(para['ingresantes'])}\n"
    return message
