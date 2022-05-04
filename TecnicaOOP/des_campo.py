"""
Desplazamiento de campo
Problema: un atributo se usa mas en otra clase
Solucion: mover el atributo a la otra clase
Causa: la extraccion de clase mueve(o no )campos

Un campo debe estar en el msimo sitio que los metodos que lo usan
"""
class clase_a:
    def __init__(self, atributo):
        self.atributoa = atributo

class clase_b:
    def __init__(self, atributo,atributoa):
        self.atributob = atributo
        self.atributoa = atributoa


"""
code smells que resuelve
- cirugia de perdigones
- jerarquias de herancia paralelas
- initimidad inapropiada

ayuda en
- extraer clase
- clase en linea
"""



    
    
