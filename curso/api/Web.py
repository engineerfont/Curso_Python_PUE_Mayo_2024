import os
import requests
import shutil

def html_from(url):
    return requests.get(url).text

def download(url, name_file):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        path, _ = os.path.split(name_file)
        os.makedirs(path, exist_ok=True)
        with open(name_file, 'wb') as file:
            shutil.copyfileobj(response.raw, file)

