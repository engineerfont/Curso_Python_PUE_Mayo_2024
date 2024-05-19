# Tipos de literales numéricos enteros
# - En base decimal:     16
# - En base binario:     0b1111
# - En base octal:       0o17
# - En base hexadecimal: 0xf

b = 0b1111  # 0..1
o = 0o17    # 0..8
h = 0xf     # 0..9, a..f

print(b)
print(h)
print(o)

a = 20
b = 71
c = 105

ab = bin(a) # Convertir a binario
ao = oct(b) # Convertir a octal
ah = hex(a) # Convertir a hexadecimal

print(ab)
print(ao)
print(ah)

# Tipos de literales de tipo caracter
# - En base ASCII:          "L"
# - En base Unicode 16-bit  "\u0394"
# - En base Unicode 32-bit  "\U00000394"

c = "\u0394"
print(type(c))
print(ord(c))

g = chr(12345)
print(g)

palabra = "mañana" # Formato iso-8859-1
# Convertir a utf-8
nueva = palabra.encode(encoding="utf-8")
print(nueva)

# Convertir a iso-8859-1
palabra = nueva.decode(encoding="utf-8")
print(palabra)

# Tipo de dato nulo en Python
# - None

nulo = None

