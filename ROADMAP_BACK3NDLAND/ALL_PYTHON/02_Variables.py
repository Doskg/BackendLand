# Son contenedores que nos permiten guardar datos. de diferentes tipos.
# Que son las variables.

a = 2  # se le asigna un valor
b = a + 1  # los valores se leen de izq a derecha.
b = 5

print(b)
# constantes = no cambian su valor.
# REGLAS.
"""
1.No puede tener espacios.
ejemplo: fecha de nacimiento.
2.No puede empezar con numeros
ejemplo: 2doEmail
3.No puede ser una palabra reservada del Lenguaje./ el nombre tiene que ser adecuado al dato.
ejemplo:if, while etc.



"""
# Convencion de Nombres.
"""
1-camelCase=> variables
Def:la primera letra de la palabra es minuscula y la primera letra de la segunda palabra es Mayus
ejemplo:fechaDeNacimiento
2-snake_case
Def:las palabras se separan por guion bajo (_)
ejemplo:snake_case
3-SCREAMING_SNAKE_CASE
Def:Se separan con guiones bajos pero para constantes, tiene que estar en MAY.
ejemplo:SOY_UNA_CONSTANTE
4-kebab-case
Def: palabras que se separan por guiones (-)
Ejemplo:soy-variable

5-l33t
ejemplo: P445W0RD

6-Notacion Hungara
ejemplos:Cadena de Txt.

"""

# todos los lenguajes de programacion se diferencia por tipado fuerte o tipado debil

"""
los lenguajes de tipado fuerte no nos dejan guardar cualquier tipo de dato sin 
declararlo antes por ejemplo hay que declarar que cosa es... por ejemplo si es fruta o verdura o es un objeto o es una persona o es 
INT
STR
Float... etc
antes de almacenar o usarlo// 
y asi determinar el tipo de dato, 
pero que pasa si quiero cambiar de entero a float o char en la misma variable, o cajita o el contenedor mismo...
no me dejaria ya que es fuertemente tipado y cuando se declara la variable solo aceptaria el dato con el que fue declarado inicialmente.
 

"""
nombre = "lucas"
nombre = "pedro"
edad = 30
print("Hola mundo soy " + nombre + "y tengo" + str(edad) + " años") #str(edad)=> convierte el valor int en una cadena , ya que el valor de (edad) es entero

#error que nos dio la linea 63
"""
  File "c:\Users\Oscar Gonzalez\Documents\GitHub\BackendLand\ROADMAP_BACK3NDLAND\ALL_PYTHON\02_Variables.py", line 63, in <module>
    print("Hola mundo soy " + nombre + "y tengo" + edad + " a�os")
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
TypeError: can only concatenate str (not "int") to str

"""
print()