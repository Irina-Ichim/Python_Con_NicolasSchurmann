# Ejemplo de funciones lambda en Python

# Sintaxis básica de una función lambda:
# lambda argumentos: expresión

# Ejemplo 1: Función lambda para sumar dos números
sumar = lambda x, y: x + y
print("Suma:", sumar(5, 3))  # Debería imprimir 8

# Ejemplo 2: Función lambda para encontrar el cuadrado de un número
cuadrado = lambda x: x**2
print("Cuadrado:", cuadrado(4))  # Debería imprimir 16

# Ejemplo 3: Función lambda en una lista (ordenar por la segunda letra)
palabras = ['manzana', 'banana', 'cereza', 'dátil', 'uva']
palabras.sort(key=lambda palabra: palabra[1])
print("Palabras ordenadas por la segunda letra:", palabras)

# Ejemplo 4: Función lambda en una lista (filtrar números pares)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda num: num % 2 == 0, numeros))
print("Números pares:", pares)

# Ejemplo 5: Función lambda en un diccionario
personas = [{'nombre': 'Alice', 'edad': 30}, {'nombre': 'Bob', 'edad': 25}, {'nombre': 'Charlie', 'edad': 35}]
personas.sort(key=lambda persona: persona['edad'])
print("Personas ordenadas por edad:", personas)

# Las funciones lambda son especialmente útiles cuando necesitas pasar una función simple como argumento a otra función
# (por ejemplo, map(), filter(), sorted(), etc.), lo que las hace versátiles en situaciones de programación funcional.