mascotas = [ "Chuchy", "Pelusa", "King", "Pulga"]
print(mascotas)

# accediendo a los elementos
print(mascotas[0])
mascotas[3] = "Bicho"   # cambia el valor de un elemento
# print(mascotas)

# # ahora solo quiero obtener parte de mi listado
# print(mascotas[:3]) # te devuelve desde el elemento 0 a 3
# print(mascotas[1:3])
# print(mascotas[2:])
# print(mascotas[-1]) # te devuelve bicho por que al no tener nada a la izquierda, se va la derecha donde tengo bicho
# print(mascotas[-2])
# print(mascotas[::2]) # queremos acceder a los elementos pares

numeros = list(range(21))
print(numeros)
print(numeros[::2])  # devuelve los elementos pares
print(numeros[::3])  # devuelve los elementos de 3 en 3
print(numeros[1::2]) # devuelve los numeros impares

# Otra forma para devolver impares
numeros1 = list(range(1,21))
print(numeros1[::2])