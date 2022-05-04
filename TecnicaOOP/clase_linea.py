"""
clase en linea
Problema: una clse no hace nada, ni se espera
Solucion: mover sus entidades a otra clase
Causa: la clase fue perdiendo responsabilidad
Beneficios: liberar espacion en la memoria
"""
# ejemplo:
class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    

class Direccion:
    def __init__(self, direccion):
        self.direccion = direccion

    def get_linea_direccion(self):
        return "{}".format(self.direccion)

## refactorizacion crear un nueva clase
class Cliente:
    def __init__(self, nombre, apellido, edad,direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion


"""
code smells que resuelve
- cirugi de perdigones
- jerarquias de herencia paralelas
- intimidad inapropiada
"""