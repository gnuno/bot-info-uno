import requests
import json

with open('./assets/calendario_academico.json') as f:
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
for item in calendario:
    message += f"{item['titulo']}\n"
    para = item['actividades']['para']
    if 'regulares' in para:
        message += f"Regulares\n"
        message += f"{get_dates(para['regulares'])}\n"
    if 'ingresantes' in para:
        message += f"Ingresantes\n"
        message += f"{get_dates(para['ingresantes'])}\n"
print(message)

# print(item['actividades']['para']['regulares'])
