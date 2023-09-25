# Creamos una lista vacía
mi_lista = []

# Agregamos elementos a la lista usando el método .append()
mi_lista.append("Manzana")
mi_lista.append("Banana")
mi_lista.append("Cereza")

# Imprimimos la lista después de agregar elementos
print(mi_lista)

# Creamos dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Usamos el método .extend() para agregar los elementos de lista2 a lista1
lista1.extend(lista2)

# Imprimimos la lista1 después de la extensión
print(lista1)

# Creamos una lista inicial
mi_lista = [1, 2, 3, 4]

# Usamos el método .insert() para insertar el número 5 en la posición 2
mi_lista.insert(2, 5)

# Imprimimos la lista después de la inserción
print(mi_lista)

# Creamos una lista con elementos duplicados
mi_lista4 = [1, 2, 3, 4, 2, 5, 6]

# Usamos el método .remove() para eliminar el valor 2 de la lista
mi_lista4.remove(2)

# Imprimimos la lista después de la eliminación
print(mi_lista4)

frutas = ["manzana", "banana", "naranja", "uva"]

# Eliminar y obtener el elemento en la posición 1 (banana)
elemento_eliminado = frutas.pop(1)

print("Elemento eliminado:", elemento_eliminado)
print("Lista actualizada:", frutas)

colores = ["rojo", "verde", "azul", "amarillo"]

# Encontrar el índice de "azul" en la lista
indice = colores.index("azul")

print("El índice de 'azul' es:", indice)

numeros = [1, 2, 3, 2, 4, 2, 5]

# Contar cuántas veces aparece el número 2 en la lista
conteo = numeros.count(2)

print("Número de veces que aparece el 2:", conteo)

numeros = [4, 2, 7, 1, 9, 5]

# Ordenar la lista en orden ascendente
numeros.sort()

print("Lista ordenada:", numeros)

frutas = ["manzana", "banana", "naranja", "uva"]

# Invertir el orden de los elementos en la lista
frutas.reverse()

print("Lista invertida:", frutas)
