# pip install requests
# pip3 install requests
# python3 -m pip install requests

import requests

url = 'https://www.pue.es'

html = requests.get(url).text

print(html)
