import requests
import json


def function_with_optional(*args):
    if len(args) > 0:
        print('Tengo args')
    else:
        print('No tengo args')


cadena = '/mails informatica'
cadena2 = '/mails'

list1 = cadena.split()
list2 = cadena2.split()

function_with_optional(cadena2)
function_with_optional()
