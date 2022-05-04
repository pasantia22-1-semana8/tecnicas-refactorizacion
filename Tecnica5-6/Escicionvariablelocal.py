"""
Escision de variable local
Problema: variable local reutilizable
Solucion: crear una variable para cada caso
Causa: es peligroso, confuso
Beneficios: responsabilidad unica, legibilidad
"""
## ejemplo
alto =2
ancho = 3
#-----------------
temp = 2 * (alto + ancho)
print("el perimetro:",temp)

temp = alto * ancho;
print("el area es:",temp)

## refactorizacion

perimetro = 2 * (alto + ancho)
print("el perimetro:",perimetro)

area = alto * ancho;
print("el area es:",area)

"""
relacion con otras tecnicas
Opuesta: variable local en linea

Similares: 
    Extraccion de variable
    eliminacion de asignaciones a parametros
Ayuda: extraccion de metodo.
"""
