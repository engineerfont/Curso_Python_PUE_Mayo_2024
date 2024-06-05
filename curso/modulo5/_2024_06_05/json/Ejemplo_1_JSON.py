import json
import datetime

empleado = {
    "id": 4,
    "nombre": "María Mercedes",
    "departamento": "HR",
    "fecha": datetime.datetime.today()
}

def convert_timestamp(item_date_object):
    if isinstance(item_date_object, (datetime.date, datetime.datetime)):
        return item_date_object.timestamp()

def to_json(schema):
    return json.dumps(schema, default=convert_timestamp)

def to_schema(field):
    field['fecha'] = datetime.datetime.fromtimestamp(float(field['fecha']))
    return field

# Convertir diccionario python a cadena JSON
json_string = to_json(empleado)
print(json_string)

c_json = json.loads(json_string)
print(c_json)
#print(type(c_json))

#c_json['fecha'] = datetime.datetime.fromtimestamp(float(c_json['fecha']))
#print(c_json)

print(to_schema(c_json))
