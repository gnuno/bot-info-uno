import requests
import json
from unidecode import unidecode

accented_string = u'Málaga'

unaccented_string = unidecode(accented_string).lower()
print(unaccented_string)

with open('./assets/mails_escuelas.json', encoding='utf-8') as f:
    mails = json.load(f)


def filter_mail(term):

    result = filter(lambda x: term in x['escuela'], mails)
    return list(result)


print(filter_mail('informatica'))
