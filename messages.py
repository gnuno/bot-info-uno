LINKS_ROOT_URL = 'https://gea-uno.github.io/'


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
            message += f"<b>Informática</b>: {LINKS_ROOT_URL}/{name}\n"
        elif name == 'enf':
            message += f"<b>Enfermería</b>: {LINKS_ROOT_URL}/{name}\n"
        elif name == 'admin':
            message += f"<b>Administración</b>: {LINKS_ROOT_URL}/{name}\n"
        elif name == 'hum':
            message += f"<b>Humanidades</b>: {LINKS_ROOT_URL}/{name}\n"
        elif name == 'ingq':
            message += f"<b>Ing. Química</b>: {LINKS_ROOT_URL}/{name}\n"
        elif name == 'links':
            message += f"<b>Plataformas UNO</b>: {LINKS_ROOT_URL}/uno\n"
        elif name == 'info-comun':
            message += f"<b>Comunidades IT</b>: {LINKS_ROOT_URL}/info/{name}\n"

    message += f"\nY acá te dejamos el dashboard principal por si querés chusmear desde cero!\n{LINKS_ROOT_URL}"
    return message
