numeros = [1, 2, 3]

# Desenpaquetar la lista creando variables en posiciones concretas
# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)


#  El concepto de desempaquetar secuencias en Python usando el operador *,
#  que se conoce como "desempaquetado extendido" o "desempaquetado de asterisco".
#  Esto se utiliza para asignar partes específicas de una secuencia, como una lista, a variables individuales.
# si queremos obtener unicamente el primer elemento de nuestro listado

primero, *otros = numeros
print(primero)
print(primero, otros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros= numeros
print(primero, segundo, otros)

# ahora quiero imprimir el primer elemento y el ultimo
primero, *otros, ultimo = numeros
print(primero, ultimo)
