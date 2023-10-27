# en listas puedees agregar palabras, letras, numeros, sublistas y las puedes juntar

numeros = [1, 2, 3] # se escriben con [ ]
letras = ["a", "b", "c"]
palabras = [ "chanchito", "feliz"]
palabrasFelices = ["chanchito", "feliz", "Felipe", "alumno" ]
# print(numeros, letras, palabras, palabrasFelices)
booleans = [ True, False, True, True]
print(booleans)

# Matriz es un listado que contiene mas listados
matriz = [[0,1], [1, 0]]

ceros = [0, 1] * 10
print(ceros)

alfanumerico = numeros + letras
print(alfanumerico)

# rango = list(range(11))  # range te lo lleva todo de cero hasta tu valor-1
# si no quieres ver el valor 0 le debes indicar tu desde donde quieras que empieza
rango = list(range(1, 11))  
# print(rango)

chars = list("hola mundo") # te separa lo que tengas en tu lista letra por letra, te incluye los espacios
print(chars)