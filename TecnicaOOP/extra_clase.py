"""
extraccion de clase
Problema: una clase trabaja por dos
Solucion: crear una nueva clase, con sus atributos, metodos
Causa; todas las clases empeizan simples, luego se expanden
Beneficios: principio de unica responsabilidad: codigo comprensible,obvio,
tolerante al cambio,fiable.
"""
# ejemplo:
class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.poblacion = "Madrid"
        self.codigo_postal = 28001
        self.direccion = "Calle de la calle"
        self.calles = "Calle de la calle"
        self.zona = "Centro"
    

## refactorizacion crear un nueva clase
class Direccion:
    def __init__(self, poblacion, codigo_postal, direccion, calles, zona):
        self.poblacion = poblacion
        self.codigo_postal = codigo_postal
        self.direccion = direccion
        self.calles = calles
        self.zona = zona

    def get_linea_direccion(self):
        return "{} {} {}".format(self.direccion, self.calles, self.zona)


"""
code smells que resuelve
- intimiadad inapropiada
- clase grande
- agrupaciones de datos
- campos temporales
- clase alternativas con diferentes interfaces
- codigo duplicado
- cambio divergente

Opueta a clase en linea

similar extraer subclase
"""