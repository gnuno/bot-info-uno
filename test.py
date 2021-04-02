import requests
import json

with open('./assets/calendario_academico.json', encoding='utf-8') as f:
    calendario = json.load(f)


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


message = f"El calendario acádemico es el siguiente:\n\n"
matches = ['Inscripción a Carreras de Grado', 'Exámenes Turno']
for item in calendario:
    message += f"<b><u>{item['titulo']}</u></b>\n"
    print(item['titulo'])
    para = item['actividades']['para']
    isMatch = [True for x in matches if x in item['titulo']]
    if 'regulares' in para:
        if True not in isMatch:
            print('IF REGULARES')
            message += f"<b>Regulares</b>\n"
        message += f"{get_dates(para['regulares'])}\n"
    if 'ingresantes' in para:
        if True not in isMatch:
            print('IF INGRESANTES')
            message += f"<b>Ingresantes</b>\n"
        message += f"{get_dates(para['ingresantes'])}\n"
# print(message)

# print(item['actividades']['para']['regulares'])
