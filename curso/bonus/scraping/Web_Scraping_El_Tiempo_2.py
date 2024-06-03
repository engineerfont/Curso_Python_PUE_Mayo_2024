from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from bs4 import BeautifulSoup

import time
import datetime
import os

import curso.api.Data as Data
import curso.api.Ficheros as Files
import curso.api.Cadena as Cadena
import curso.api.Texto as Texto
import curso.api.Input as Input

SCHEMA_PROVINCIA = {}
SCHEMA_PROVINCIA['id'] = Input.to_int
SCHEMA_PROVINCIA['provincia'] = Input.to_str
SCHEMA_PROVINCIA['id_ccaa'] = Input.to_int
SCHEMA_PROVINCIA['nombre'] = Input.to_str
SCHEMA_PROVINCIA['formato'] = Input.to_int

SCHEMA_POBLACION = {}
SCHEMA_POBLACION['id'] = Input.to_int
SCHEMA_POBLACION['id_ccaa'] = Input.to_int
SCHEMA_POBLACION['id_provincia'] = Input.to_int
SCHEMA_POBLACION['poblacion'] = Input.to_str
SCHEMA_POBLACION['nombre'] = Input.to_str
SCHEMA_POBLACION['url'] = Input.to_str
SCHEMA_POBLACION['visitada'] = Input.to_int

SCHEMA_DATA = {}
SCHEMA_DATA['fecha'] = Input.to_date
SCHEMA_DATA['id_ccaa'] = Input.to_int
SCHEMA_DATA['id_provincia'] = Input.to_int
SCHEMA_DATA['id_poblacion'] = Input.to_int
SCHEMA_DATA['hora'] = Input.to_str
SCHEMA_DATA['temperatura'] = Input.to_float
SCHEMA_DATA['viento'] = Input.to_float

RUTA_BASE_ELTIEMPO = 'c:/datasets/data/eltiempo/'
RUTA_DATASETS_POBLACIONES = RUTA_BASE_ELTIEMPO + 'poblaciones/'

FILE_DATA_PROVINCIAS = RUTA_BASE_ELTIEMPO + 'provincias.data'
FILE_DATA_POBLACIONES = RUTA_BASE_ELTIEMPO + 'poblaciones.data'
FILE_DATA_TEMPERATURAS = RUTA_BASE_ELTIEMPO + 'temperaturas.data'

URL_SITE_EL_TIEMPO = 'https://www.eltiempo.es/'


# función que recibe una colección tipo diccionario, agrega un nuevo campo 'url' a la colección y
# devuelve la colección modificada
def to_url_eltiempo(data):
    # https://www.eltiempo.es/cantabria - formato 0
    # https://www.eltiempo.es/en-provincia-huelva - formato 1
    # https://www.eltiempo.es/melilla.html - formato 2
    url = ''
    if data['formato'] == 1:
        url = 'en-provincia-' + data['nombre']
    elif data['formato'] == 2:
        url = data['nombre'] + '.html'
    else:
        url = data['nombre']
    data['url'] = URL_SITE_EL_TIEMPO + url
    return data


# función que recibe una colección de tipo diccionario y devuelve los valores de la colección como una cadena de texto
def dict_to_string(data):
    return ';'.join(str(value) for value in data.values())


# función que devuelve todas las poblaciones del sitio web 'eltiempo.es'
def extraer_poblaciones_eltiempo(url_site, web_provincias):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url_site)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a._10qqh8uq'))).click()
        id_poblacion = 0
        header = ';'.join(SCHEMA_POBLACION.keys())
        for provincia in web_provincias:
            if provincia['formato'] == 2:
                continue
            print('Extrayendo de => ' + provincia['url'])
            driver.get(provincia['url'])
            time.sleep(5)
            scroll_origin = ScrollOrigin.from_viewport(10, 10)
            ActionChains(driver).scroll_from_origin(scroll_origin, 0, 1200).perform()
            ActionChains(driver).scroll_from_origin(scroll_origin, 0, 100).perform()
            data_poblaciones = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article.modules.m_ccaaprovince.m39')))
            links = [(str(tag.get_attribute('href')), tag.text) for tag in data_poblaciones.find_elements(By.TAG_NAME, 'a')]
            poblaciones = []
            for url, text in links:
                id_poblacion += 1
                poblacion = {}
                poblacion['id'] = id_poblacion
                poblacion['id_ccaa'] = provincia['id_ccaa']
                poblacion['id_provincia'] = provincia['id']
                poblacion['poblacion'] = text
                poblacion['nombre'] = url.split('/')[-1].split('.')[0]
                poblacion['url'] = url
                poblaciones.append(poblacion)
            poblaciones = map(dict_to_string, poblaciones)
            Files.save_file_list(RUTA_DATASETS_POBLACIONES + provincia['nombre'] + '.data', poblaciones, header=header)
    finally:
        driver.quit()


def get_by_id(id, collection):
    return list(filter(lambda c: c['id'] == id, collection))[0]


def merge(directory):
    data = []
    for file in Files.dir_files(directory):
        data += Data.data_record(file, header=True, schema=SCHEMA_POBLACION)
    return data


def remove_duplicate(collection, field):
    value = ''
    data = []
    for item in collection:
        data_field = Texto.to_abc(item[field])
        if data_field == value:
            continue
        value = data_field
        data.append(item)
    return data


def temperaturas_diarias(driver, poblacion, fecha=None):
    body = driver.execute_script('return document.body')
    soup = BeautifulSoup(body.get_attribute('innerHTML'), 'lxml')
    fecha = fecha if fecha else datetime.date.today()

    temperaturas = []
    for li in soup.find_all('ul', id='meteograma')[0].find_all('ul')[1].find_all('li'):
        datos = Cadena.trim(li.text).split(' ')
        data = {}
        data['fecha'] = fecha
        data['id_ccaa'] = Input.to_int(poblacion['id_ccaa'])
        data['id_provincia'] = Input.to_int(poblacion['id_provincia'])
        data['id_poblacion'] = Input.to_int(poblacion['id'])
        data['hora'] = datos[0]
        data['temperatura'] = Input.to_float(datos[1][:-1])
        data['viento'] = Input.to_float(datos[5])
        temperaturas.append(data)
    return temperaturas


def extraer_poblaciones():
    dataset_provincias = Data.data_record(FILE_DATA_PROVINCIAS, header=True, schema=SCHEMA_PROVINCIA)
    web_provincias = list(map(to_url_eltiempo, dataset_provincias))
    extraer_poblaciones_eltiempo(URL_SITE_EL_TIEMPO, web_provincias)
    dataset_poblaciones = merge(RUTA_DATASETS_POBLACIONES)
    print(len(dataset_poblaciones))

    dataset_poblaciones = map(dict_to_string, dataset_poblaciones)
    header = ';'.join(SCHEMA_POBLACION.keys())
    Files.save_file_list(FILE_DATA_POBLACIONES, dataset_poblaciones, header=header)

    dataset_poblaciones = Data.data_record(FILE_DATA_POBLACIONES, header=True, schema=SCHEMA_POBLACION)

    print(len(dataset_poblaciones))
    dataset_poblaciones = remove_duplicate(dataset_poblaciones, 'nombre')
    print(len(dataset_poblaciones))

    header = ';'.join(SCHEMA_POBLACION.keys())
    dataset_poblaciones = map(dict_to_string, dataset_poblaciones)
    Files.save_file_list(FILE_DATA_POBLACIONES, dataset_poblaciones, header=header)


def temperaturas_provincia(id_provincia, numero=None, fecha=None):
    numero = numero if numero else 10
    fecha = fecha if fecha else datetime.date.today()
    dataset_provincias = Data.data_record(FILE_DATA_PROVINCIAS, header=True, schema=SCHEMA_PROVINCIA)
    dataset_poblaciones = Data.data_record(FILE_DATA_POBLACIONES, header=True, schema=SCHEMA_POBLACION)

    provincia = get_by_id(id_provincia, dataset_provincias)

    driver = webdriver.Chrome()

    poblaciones_visitadas = []

    FILE_POBLACIONES_VISITADAS = RUTA_BASE_ELTIEMPO + Cadena.date_to_string(fecha) + '_temperaturas_visitadas.data'
    if os.path.exists(FILE_POBLACIONES_VISITADAS):
        poblaciones_visitadas = list(map(lambda l: int(l.strip()), Files.list_file_text(FILE_POBLACIONES_VISITADAS)))

    try:
        driver.get(URL_SITE_EL_TIEMPO)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a._10qqh8uq'))).click()

        if not os.path.exists(FILE_DATA_TEMPERATURAS):
            with open(FILE_DATA_TEMPERATURAS, mode='w', encoding='utf-8') as file:
                file.write(';'.join(SCHEMA_DATA.keys()) + '\n')

        dataset = list(filter(lambda poblacion: poblacion['id_provincia'] == provincia['id'], dataset_poblaciones))

        for n, poblacion in enumerate(dataset):
            if n == numero:
                break
            if poblacion['id'] in poblaciones_visitadas:
                continue
            url = poblacion['url'] + '?v=por_hora'
            print(f"{provincia['provincia']} [{n + 1}:{len(dataset)}] '{poblacion['poblacion']}' => {url}")
            driver.get(url)
            time.sleep(5)
            temperaturas = temperaturas_diarias(driver, poblacion, fecha)
            dataset_temperaturas = list(map(dict_to_string, temperaturas))
            Files.save_file_list(FILE_DATA_TEMPERATURAS, dataset_temperaturas, mode='a')
            poblaciones_visitadas.append(poblacion['id'])
    finally:
        Files.save_file_list(FILE_POBLACIONES_VISITADAS, poblaciones_visitadas)
        driver.quit()


temperaturas_provincia(2)
