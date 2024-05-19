def padding(valor, caracter, posiciones):
    cad = str(valor)
    if len(cad) >= posiciones:
        return cad
    resta = posiciones - len(cad)
    izq = resta // 2
    der = resta - izq
    cad_izq = caracter * izq
    cad_der = caracter * der
    return cad_izq + cad + cad_der

print(padding(293, '=', 12))  # ==29===


