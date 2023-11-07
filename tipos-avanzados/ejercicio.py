from pprint import pprint


# Ejercicios con Nicolas
# eliminar los espacios en blanco de un string.
# haremos una comprension de listas
string = " Hola mundo este es mi string"

def quita_espacios(texto):
    return[ char for char in texto if char != " "]

def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict  

def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )  
 
def mayores_tuplas(lista):
    maximo = lista[0][1] 
    respuesta = {}
    for orden in lista:
         if maximo > orden[1]:
             break  
         respuesta[orden[0]] = orden[1] 
    return respuesta     
    
def crea_mensaje(diccionario):
    mensaje = "Los que más se repitden son: \n" 
    for key, valor in diccionario.items():
        mensaje  += f"- {key} con {valor} repeticiones \n"  
    return mensaje

sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
# print(sin_espacios)
# pprint(contados, width =1)
# print(ordenados)
print(mayores)
print(mensaje)

#Ejercicio 2
# Contar en un diccionario cuantas veces se repite los caracteres de un strings
#pprint significa "pretty-print", y es una función que se utiliza para imprimir estructuras de datos en un formato más legible y organizado en la consola. La línea from pprint import pprint importa la función pprint del módulo pprint para que puedas usarla en tu código.

#La función pprint es especialmente útil cuando deseas imprimir estructuras de datos complejas, como diccionarios o listas anidadas, en lugar de simplemente imprimirlos
# con print. Ayuda a formatear los datos de manera que sean más fáciles de leer en la consola.

#El segundo argumento de pprint, width, controla el ancho máximo de la línea en la salida impresa. Cuando se pasa el argumento width, pprint intenta ajustar los datos
# para que se ajusten dentro de ese ancho máximo. Si los datos no caben en una línea dentro del ancho especificado, pprint dividirá la línea para mantenerla dentro del
# límite, lo que hace que la salida sea más fácil de leer.

# Aquí tienes un ejemplo de cómo se usa pprint con el argumento width:

# from pprint import pprint

# contados1 = {'manzanas': 10, 'peras': 5, 'bananas': 12, 'uvas': 8}

# pprint(contados, width=20)

#En este caso, pprint formateará la salida para que se ajuste dentro de un ancho máximo de 20 caracteres por línea. Esto puede ser útil para imprimir estructuras
# de datos largas o anidadas de una manera más organizada y legible en la consola.

#Ejercicio3 ordenar las llaves de un diccioanrio por el valor que tiene y devolver una lista de tuplas

# Ejercicio4 de un listado de tuplas, devolver las tuolas que tengan el mayor valor

# Ejercicio5 Crear un mensaje que diga: Los caracteres que mas se reptan con 4 repeticiones son C y D

# \n recuerda que significa una nueva linea