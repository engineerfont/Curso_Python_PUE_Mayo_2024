import curso.api.Constantes as Const
import curso.modulo5._2024_06_03.modulos.Modulo_1 as prueba

def incrementar2(numero):
    #global Const.PI
    Const.PI += 1
    return numero + Const.PI

print(prueba.incrementar(5))
print(incrementar2(5))
