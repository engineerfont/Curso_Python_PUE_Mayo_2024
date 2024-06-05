import json
import datetime
import random

empleado_detalles = {
    "id": 4,
    "nombre": "María Mercedes",
    "departamento": {
        "seccion": "HR",
        "ingreso": datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "puesto": "Gerente"
    },
    "fecha": datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
}

datos_persona = {
    "nombre": "Amalia de los Ríos",
    "edad": 30,
    "altura": 1.74,
    "estado": True,
    "direccion": {
        "calle": "Real, 25",
        "poblacion": "Quintana Redonda",
        "provincia": "Soria"
    }
}

datos_persona['numeros'] = [random.randint(1, 100) for n in range(1, 10, 2)]
datos_persona['empleado'] = empleado_detalles

# Convertir diccionario python a cadena JSON
json_string = json.dumps(datos_persona)
print(json_string)

# Convertir cadena JSON a diccionario python
persona_datos = json.loads(json_string)
print(persona_datos)

print(f'Nombre => {persona_datos['nombre']}')

poblacion = persona_datos['direccion']['poblacion']
print(f'Población => {poblacion}')

fecha = persona_datos['empleado']['departamento']['ingreso']
print(f'Fecha de ingreso empleado => {fecha}')

puesto = persona_datos['empleado']['departamento']['puesto']
print(f'Puesto de empleado => {puesto}')
