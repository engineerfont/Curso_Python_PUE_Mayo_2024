# Crear una aplicación que dada la siguiente url
# https://www.boe.es/boe/dias/2024/05/29/
# Descargar todos los pdfs que contenga el documento HTML

import curso.api.Web as Web

base = 'https://www.boe.es'

url = 'https://www.boe.es/boe/dias/2024/05/29/'

html = Web.html_from(url)

def extract(html, atributo, urls=[]):
    posicion = html.find(atributo)
    if posicion == -1:
        return urls
    else:
        url = html[posicion:]
        # href=http://www.doini.com>mi dominio ....
        url = url.split(' ')[0].split('>')[0].split('=')[1].strip()
        urls.append(url)
        html = html[posicion + len(atributo):]
        return extract(html, atributo, urls)

#enlaces = extract(html.replace('"', '').replace("'", ""), 'href')
#pdfs = map(lambda w: base + w if w.startswith('/') else w, filter(lambda e: e.endswith('.pdf'), enlaces))

#print(list(pdfs))

lista = ['a', 'r', 't']
nueva = list(enumerate(lista, start=12))
print(nueva)

