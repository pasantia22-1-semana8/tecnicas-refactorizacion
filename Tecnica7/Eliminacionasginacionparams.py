"""
Eliminacion asignacion de parametros.
Problema: parametro modificado
Solucion: usar una varible en vez del parametro.
Causa: es peligros, confuso.
Beneficios: reponsablida unica, legibilidad.
"""
## ejemplo

MIN_DES=5
DESC=3
#-----------------

def descuento(entrada,cantidad):
    if(cantidad > MIN_DES):
        entrada = cantidad * (1-DESC) 

## refactorizacion

def descuento_ref(entrada,cantidad):
    res = entrada
    if(cantidad>MIN_DES):
        res = cantidad * (1-DESC)

"""
Similar: Escicion de variable local

Ayuda: extraccion de metodo.
"""