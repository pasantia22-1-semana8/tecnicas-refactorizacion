"""
Metodo en linea (opuesta al metodo de extraccionmetodo)
Problema: cuerpo dle metodo mas obvio
Solucion: Reemplazar llamdas por cuerpo del metodo
Causa: la delegacion ya no aportaba nada.
Beneficios: Reducir la cantidad de metodos innecesarios nos deja un codigo mas directo. 
"""
arr = [1,2,3]

## ejemplo
def calcular_arrglo(arr):
    contador = len(arr)
    if(entre_tres_cinco_lineas(contador)):
        print(arr)
        ##......

def entre_tres_cinco_lineas(contador):
    return contador >=3 and contador <=5

calcular_arrglo(arr)

## refactorizacion
def calcular_arreglo_ref(arr):
    contador = len(arr)
    if(contador >=3 and contador <=5):
        print(arr)

calcular_arreglo_ref(arr)