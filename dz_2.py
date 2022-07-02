import requests
import unittest


TOKEN = ' '

URL = 'https://cloud-api.yandex.net/v1/disk/resources'

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    x = requests.put(f'{URL}?path={path}', headers=headers)
    return x.status_code

