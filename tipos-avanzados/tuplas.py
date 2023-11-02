numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# crear una nueva tupla concatenando 2 tuplas
# las tuplas son inmutables

# la funcion tuple modifica una lista en tupla, recibe cualquier tipo de datos iterables
punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)
    
# las tuplas no se deben modificar pero si lo necesitas modificar utiliza la funcion list()
listaNumeros = list(numeros)
print(listaNumeros)
