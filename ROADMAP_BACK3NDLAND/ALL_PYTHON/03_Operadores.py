# Diagramas de flujo, para entender Operadores.

"""
Operador     ----   Descripcion    ----    Ejemplos
  ==                Igual                         
 """

# Ejemplo

""" 
edad = 25
if(edad >= 18) and (edad < 70)  ==>True

NOT ((edad <18 ) or (edad >=70)) ==> True
"""


edad = 18
if edad >= 18:
    print("mayor de edad")

else:
    print("menor de edad")
