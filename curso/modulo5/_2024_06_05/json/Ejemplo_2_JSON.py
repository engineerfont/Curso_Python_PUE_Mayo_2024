import json

datos_persona = {
    "nombre": "Amalia de los Ríos",
    "edad": 30,
    "direccion": {
        "calle": "Las Rozas, 176",
        "poblacion": "Barcelona",
        "provincia": "Barcelona"
    }
}

# Convertir diccionario python a cadena JSON
json_string = json.dumps(datos_persona)
print(json_string)

# Convertir cadena JSON a diccionario python
persona_datos = json.loads(json_string)
print(persona_datos)
