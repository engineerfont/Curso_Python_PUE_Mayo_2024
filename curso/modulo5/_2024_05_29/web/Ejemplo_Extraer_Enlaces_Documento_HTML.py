import curso.api.Web as Web

def extract(html, atributo, urls=[]):
    posicion = html.find(atributo)
    if posicion == -1:
        return urls
    else:
        url = html[posicion:]
        url = url.split(' ')[0].split('>')[0].split('=')[1].strip()
        urls.append(url)
        html = html[posicion + len(atributo):]
        return extract(html, atributo, urls)

def extract_urls(url):
    html = Web.html_from(url)
    html = html.replace('"', '').replace("'", "")
    return extract(html, 'href')


url = 'https://www.pue.es'
links = extract_urls(url)
print(links)
