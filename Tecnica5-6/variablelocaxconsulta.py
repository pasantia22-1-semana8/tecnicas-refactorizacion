"""
Variable local por consulta
Problema: variable local solo para resultado de expresion
Solucion: extraer expresion a metodo y llamarlo.
Causa: preparar estraer metodo, reuitlizacion
Beneficios: codigo mas legible, reducir duplicacion
inconveneintes: rendimiento en operacion pesada.
"""
from pydoc import describe


cantidad = 5
precio_unitario = 3

MIN_DESC = 2
DESC = 1
def aplicar_descuento():
    precio = cantidad * precio_unitario
    if(precio > MIN_DESC):
        return precio * (1-DESC)
    else:
        return precio


##refactorizando
def aplicar_descuento_ref():
    if(precio() > MIN_DESC):
        return precio() * (1-DESC)
    else:
        return precio()

def precio():
    return cantidad * precio_unitario

"""
similitud con la extracion de metodo

aplicar a los code smells
comentario
"""