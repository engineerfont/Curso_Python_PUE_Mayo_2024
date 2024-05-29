# Definir una función que recibe dos valores de entrada, el primer valor
# corresponde al número de datos de mujeres y el segundo valor corresponde
# al número de datos de hombres, utilizando el esquema 'SCHEMA_USUARIO'

import random
import curso.api.Texto as Texto
import curso.api.Ficheros as Files
import curso.api.Cadena as Cad
import curso.api.Mates as Mates
import curso.api.Schema as Schema
import curso.api.Data as Data

def personas(numero_mujeres, numero_hombres):
    ccaa = Data.data_record('c:/datasets/data/ccaa.data', header=True, schema=Schema.SCHEMA_CCAA)
    provincias = Data.data_record('c:/datasets/data/provincias.data', header=True, schema=Schema.SCHEMA_PROVINCIA)
    poblaciones = Data.data_record('c:/datasets/data/poblaciones.data', header=True, schema=Schema.SCHEMA_POBLACION)
    nombres = list(map(lambda s: s.strip(), Files.list_file_text('c:/datasets/data/nombres.data')[1:]))
    apellidos = list(map(lambda s: s.strip(), Files.list_file_text('c:/datasets/data/apellidos.data')[1:]))

    nifs = []
    mobiles = []
    faxes = []
    emails = []

    global id_persona
    id_persona = 0

    def get_nif():
        while True:
            number = random.randint(0, 99999999)
            nif = Cad.to_nif(number)
            if nif not in nifs:
                nifs.append(nif)
                break
        return nif

    def get_mobile():
        while True:
            ini = '6'
            fin = str(random.randint(0, 99999999)).zfill(8)
            number = int(ini + fin)
            if number not in mobiles:
                mobiles.append(number)
                break
        return number

    def get_fax():
        while True:
            ini = '9'
            fin = str(random.randint(0, 99999999)).zfill(8)
            number = int(ini + fin)
            if number not in faxes:
                faxes.append(number)
                break
        return number

    def get_date():
        d31 = [1, 3, 5, 7, 8, 10, 12]
        d30 = [4, 6, 9, 11]
        year = random.randint(1940, 2020)
        month = random.randint(1, 12)
        day = 0
        if month in d31:
            day = random.randint(1, 31)
        elif month in d30:
            day = random.randint(1, 30)
        elif month == 2:
            day = random.randint(1, 28 + (1 if Mates.es_bisiesto(year) else 0))
        return f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}'

    def get_cp(id_provincia):
        return int(str(id_provincia) + str(random.randint(1, 999)).zfill(3))

    def get_email(name):
        domain = ['gmail.com', 'outlook.com', 'hotmail.com',
                  'google.es', 'outlook.es', 'hotmail.es']
        while True:
            number = str(random.randint(1, 999)).zfill(3)
            mail = domain[random.randint(0, 5)]
            email = f'{Texto.to_email(name)}.{number}@{mail}'
            if email not in emails:
                emails.append(email)
                break
        return email

    def get_poblaciones(id_region):
        return list(filter(lambda r: r['idprovincia'] == id_region, poblaciones))

    def getById(id, records):
        return list(filter(lambda r: r['id'] == id, records))[0]

    def get_names(sex):
        filtrados = filter(lambda x: x.strip().split(';')[1] == sex, nombres)
        return list(map(lambda x: x.split(';')[0], filtrados))

    def get_record(sex):
        names = get_names(sex)
        f_surname = apellidos[random.randint(0, len(apellidos) - 1)]
        s_surname = apellidos[random.randint(0, len(apellidos) - 1)]
        global id_persona
        id_persona += 1
        data = {}
        data['id'] = id_persona
        data['nombre'] = names[random.randint(0, len(names) - 1)]
        data['apellidos'] = f'{f_surname} {s_surname}'
        data['sexo'] = sex
        data['nif'] = get_nif()
        provincia = provincias[random.randint(0, len(provincias) - 1)]
        data['ccaa'] = getById(provincia['idccaa'], ccaa).get('ccaa')
        data['provincia'] = provincia['provincia']
        poblaciones = get_poblaciones(provincia['id'])
        poblacion = poblaciones[random.randint(0, len(poblaciones) - 1)]
        data['poblacion'] = poblacion['municipio'].capitalize()
        data['cp'] = get_cp(provincia['id'])
        data['nacimiento'] = get_date()
        data['movil'] = get_mobile()
        data['fax'] = get_fax()
        data['email'] = get_email(data['nombre'])
        return data

    men = list(map(lambda r: get_record('h'), range(numero_hombres)))
    women = list(map(lambda r: get_record('m'), range(numero_mujeres)))
    records = men + women
    random.shuffle(records)
    return records

def to_string(record, sep=None):
    separator = sep if sep else ';'
    return separator.join(str(value) for value in record.values()) + '\n'

def guardar_datos(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        datos = list(map(to_string, data))
        file.writelines(datos)


data = personas(50, 50)
guardar_datos('c:/datasets/data/personas.datos', data)
