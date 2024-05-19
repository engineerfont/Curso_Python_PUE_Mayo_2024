# Ejemplos de cadenas en Python

# Las cadenas en Python o strings son un tipo inmutable que permite almacenar
# secuencias de caracteres.

# Ejemplos de cadenas en Python

# Utilizando las doble comillas
nombre = "Xoan"
print(nombre)

# Utilizando las comillas simples
nombre = 'Xoan'
print(nombre)

# Una situación que muchas veces se puede dar, es cuando queremos introducir
# una comilla, bien sea simple ' o doble " dentro de una cadena.
#frase = "Esta frase utiliza "comillas" dobles internas"

# Secuencias de escape
# Secuencia         Representa
# ----------         ----------
# \t                Tabulación
# \n                Nueva línea
# \'                Comilla simple
# \"                Comilla doble
# \\                Barra invertida
# \u                Carácter unicode (con 4 dígitos hexadecimales)
# \U                Carácter unicode (con 8 dígitos hexadecimales)

frase = "hola\t\t\thola"

# Ejemplos de secuencias de escape
frase1 = "Esta frase utiliza \"comillas\" dobles internas"
frase2 = 'Esta frase utiliza \'comillas\' dobles internas'
frase2b = 'Esta frase utiliza "comillas" dobles internas'
frase3 = 'Esta frase \t\t\tcontiene un tabulador interno'
frase4 = "La frase tiene un salto de \nlínea interno"
carpeta = 'c:\\temp\muestra\\'
frase5 = "\u00A9 Derechos de autor"
frase6 = "\U0001F604 Cara Sonriente"
print(frase1)
print(frase2)
print(frase3)
print(frase4)
print(carpeta)
print(frase5)
print(frase6)

print('-' * 80)

# Caracteres de Escape Raw (r) o (R)
# Si queremos que los caracteres de escape no sean interpretados en una
# cadena, puedemos utilizar el prefijo r para crear una cadena de escape cruda.
directorio = r"C:\Directorio\Archivo"
print(directorio)

print('-' * 80)


# Formateo de cadenas

# Para concatenar una cadena con otra utilizamos el operador +, las cadenas
# se pueden concatenar con otro tipo de variables como por ejemplo variables
# numéricas (enteras, reales y complejas), booleanas, etc.

# Concatenar una cadena con otra cadena
nombre = 'Xoan'
apellido = 'Gallego'
nome = nombre + ' ' + apellido
print(nome)

# Concatenar una cadena con una variable numérica
nombre = "Ana Manuela"
edad = 28
datos = "Nombre: " + nombre + ", Edad: " + str(edad)
print(datos)

# Concatenar una cadena con una variable booleana
nombre = "Ana Manuela"
mayor = True
datos = "Nombre: " + nombre + ", Mayor: " + str(mayor)
print(datos)

print('<>' * 80)



# Replicar o repetir una cadena con el operador '*'
palabra = 'Python '
print(palabra * 3)

print('-' * 80)

# Utilizando el carácter '%'
numero = 5
cadena = "El número es %d" % numero
print(cadena)

nombre = "Ana Manuela"
edad = 28
datos = "Nombre: %s, Edad: %d" % (nombre, edad)
print(datos)

nombre = "Ana Manuela"
mayor = True
datos = "Nombre: %s, Mayor: %s" % (nombre, mayor)
print(datos)

print('-' * 80)


# Utilizando la función 'format'
s = "Los números son {} y {}".format(5, 10)
print(s)

s = "Los números son {u} y {w}".format(w=5, u=10)
print(s)

print('-' * 80)

import curso.api.Mates as m

# Utilizando cadenas literales (f) o (F)
a = 50
b = 100
s = f"Los números son {a} y {b}"
print(s)

s = F"La suma es de {a} y {b} es {m.suma(a, b)}"
print(s)


def suma(a, b):
    return a + b


x = 200
y = 400
s = f"El resultado de la función es {suma(x, y)}"
print(s)

print('-' * 80)

# Funciones de cadenas
frase = "cadena de texto en Python"

# Convertir una cadena a mayúsculas
print(frase.upper())

# Convertir una cadena a minúsculas
print(frase.lower())

# Capitalizar una cadena de texto
print(frase.capitalize())

# Comprueba si empieza por una determinada cadena de texto
print(frase.startswith('cad'))

# Comprueba si finaliza por una determinada cadena de texto
print(frase.endswith('python'))

# Comprueba si todos los caracteres de una cadena son alfanuméricos
email = 'correo@dominio.com'
print(email.isalnum())

# Comprueba si todos los caracteres de una cadena son alfabéticos
nombre = 'Xoan'
print(nombre.isalpha())

# Comprueba si todos los caracteres de una cadena son dígitos numéricos
edad = '27'
print(edad.isnumeric())

print('-' * 80)

# Elimina por la izquierda el caracter que se le indica, si se llama sin
# parámetros elimina el espacio en blanco
frase = 'rrrrrrrHorla'
print("lstrip =>", frase.lstrip('r'))

frase2 = 'rrrrrrrggggggggHorla'
print("lstrip2 =>", frase2.lstrip('gr'))

# Elimina por la derecha el caracter que se le indica, si se llama sin
# parámetros elimina el espacio en blanco
frase = 'Holaxxxxxxxxx'
print("rstrip =>", frase.rstrip('x'))

# Elimina por la izquierda y derecha el caracter que se le indica, si se
# llama sin parámetros elimina el espacio en blanco
frase = 'xxxxxxxxxxwwwwxxxxxxxxxwww'
print("strip =>", frase.strip('xw'))

print('-' * 80)


# Rellena con ceros una cadena por la izquierda con una determinada longitud
cad = 'nueva'
print("zfill =>", cad.zfill(20))

print('-' * 80)

frase = 'Hoy es miercoles'
posi = frase.find('I', 6, 10)
print(posi)

#print(frase.index('8', 2, 7))

'''
# Devuelve una lista como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
numeros = ['1', '2', '3', '4', '5']
print("join =>", "<=>".join(numeros))

# Devuelve un conjunto como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
numeros = {'1', '2', '3', '4', '5'}
print("join =>", "<=>".join(numeros))

# Devuelve una cadena como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
frase = 'nueva frase'
print("join =>", "-".join(frase))

print('-' * 80)

# Dividir una cadena en subcadenas según un determinado carácter o caracteres
frase = 'esta-es-una-frase-a-subdividir'
print("split=>", frase.split('-'))

frase = 'esta<->es<->una<->frase<->a<->subdividir'
print("split=>", frase.split('<->'))

frase = 'esta-es---una--frase--a-----subdividir'
print("split=>", frase.split('-'))

print('-' * 80)

# Reemplazar caracteres de una cadena por otros caracteres
frase = 'frase para utilizar en el reemplazo'
print("replace=>", frase.replace(' ', '<=>'))

print('-' * 80)

# Comprobar si una determinada cadena está dentro de otra cadena
buscar = 'Py'
existe = buscar in 'Programación en Python'
print(existe)


# Buscar la posición de una cadena dentro de otra cadena con 'find'
frase = 'frase para utilizar en la búsqueda'
print("find=>", frase.find('xara'))

# Buscar la posición de una cadena dentro de otra cadena con 'index'
frase = 'frase para utilizar en la búsqueda'
print("index=>", frase.index('para'))

print(frase[4:-2:2])

frase = "       esta      frase      tiene     muchos     espacios   "
print(frase.strip().split(' '))
rdo = " ".join([g for g in frase.split(' ') if len(g) > 0])
rdo = frase.replace('a', 'A')
print(rdo)
'''