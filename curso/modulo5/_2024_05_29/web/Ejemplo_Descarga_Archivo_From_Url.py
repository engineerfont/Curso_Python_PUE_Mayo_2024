# pip install shutil
# pip3 install shutil

import os.path
import shutil
import requests

def download(url, name_file):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        path, _ = os.path.split(name_file)
        os.makedirs(path, exist_ok=True)
        with open(name_file, 'wb') as file:
            shutil.copyfileobj(response.raw, file)


url = 'https://www.pue.es/'
url = 'https://www.pue.es/resources/images/logos/logo-pue-white.png'

download(url, 'c:/datasets/data/html/logo_pue.png')
print('Descargado')
