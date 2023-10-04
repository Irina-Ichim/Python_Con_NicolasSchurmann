"""Module providing a function printing python version."""

import math 


print(math.ceil(1.1))  # el nr mas cercano hacia arriba
print(math.floor(1.66666661))    # el nr mas cercano hacia abajo
print(math.isnan(44444))

# https://docs.python.org/3/library/math.html
try:
    resultado = 1 / 0
except ZeroDivisionError:
    print("¡Oops! División por cero no permitida.")
    # Establecer resultado como NaN u otro valor especial si es necesario
    resultado = float('nan')

# Verificar si el resultado es NaN
if math.isnan(resultado):
    print("El resultado es NaN")
else:
    print("El resultado no es NaN")

print(math.pow(3, 4))  # 3 elevado a 4
print(math.sqrt(4))  # raiz cuadrada

# help(math)

print(round(1.3))  # redondea el numero
print(round(1.7))
print(round(1.5))
print(abs(-13))  # retorna el valor absoluto

print(abs(33))  # creo que no doy los espacios correctos o no se
    