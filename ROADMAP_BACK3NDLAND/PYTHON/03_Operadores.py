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


nombre = input("Hola como te llamas?.. ")
edad = 0
print("Cual es tu edad " + nombre + "...")
edad = int(
    input()
)  # input detecta str por defecto, por eso hay que poner int antes del input
edad = 20
if edad >= 18: # al ejecutar el if juega con TRUE o False
    print("Hola " + nombre + "tienes : " + str(edad) + " años, y eres mayor de edad...")

else:
    print("menor de edad")

"""
# requisitos para entrar a una montana Rusa
nombre = input("Hola como te llamas?.. ")
edad = int(input("Cuantos años tienes?.."))
masDe12 = edad >= 12

respuestaHijoDelDueño = input("Eres Hijo del Dueño?")
esHijoDelDueño = respuestaHijoDelDueño == "si"
puedePasar = masDe12 or esHijoDelDueño
if puedePasar:
    print("Usted puede pasar a la montaña Rusa")
else:
    print("Usted no puede pasar")
# Min 48 Operadores aritmeticos
# https://www.youtube.com/watch?v=swdcD6OPMlk&t=1903s
