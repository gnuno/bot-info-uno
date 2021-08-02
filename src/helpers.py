import requests
import time
import src.messages as responses


def get_links_message():
    return get_links_from_api()


def get_info(url):
    url_data = dict()
    try:
        t0 = time.time()
        r = requests.get(url)
        r.raise_for_status()
        t1 = time.time()
        url_data['status'] = r.status_code
        url_data['latency'] = int((t1-t0) * 1000)
        return url_data
    except requests.exceptions.RequestException as err:
        return url_data


def get_links_from_api():
    res = requests.get('https://igna98.alwaysdata.net/page')
    data = res.json()['data']
    mapped_list = list(map(lambda link: link['name'], data))
    return responses.links_message(mapped_list)


def url_message(url, name):
    url_data = get_info(url)
    if 'status' in url_data.keys() and url_data['status'] == 200:
        return responses.url_success_message(url_data['latency'], name)
    else:
        return responses.url_failure_message(name)
