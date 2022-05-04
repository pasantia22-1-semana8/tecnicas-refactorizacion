"""
Desplazamiento de metodo
Problema: un metodo se usa mas en otra clase
Solucion: mover el metodo a la otra clase
Causa: aumentar cohesion interna y reducir dependencia.

"""


class clase_a:
    
    def metodo_a():
        print("metodo clase a")
        #logica metodo


class clase_b:
    def metodo_b():
        print("metodo de clase b")
    def metodo_a():
        print("utilizar metodo clase a")





"""
code smells que resuelve
- sentencias switch
- clase de datos
- cirugia de perigones
- jerarquias de herencia paralelas
- Envidia de caracteristicas
- intimidad inapropiada
- cadenas de mensajes

ayuda: 
extraer clase
clase en linea
introduccin de objetos de parametros.

similares:
Extraer metodo
desplazar campo
"""