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

download(url, 'c:/datasets/data/html/pue.html')
print('Descargado')
