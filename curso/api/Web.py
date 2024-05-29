import requests

def html_from(url):
    return requests.get(url).text

