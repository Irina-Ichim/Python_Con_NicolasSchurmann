mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Obtener una lista de las claves en el diccionario
claves = mi_diccionario.keys()

print("Claves del diccionario:", claves)


# Obtener una lista de los valores en el diccionario
valores = mi_diccionario.values()

print("Valores del diccionario:", valores)


# Obtener una lista de tuplas (clave, valor) en el diccionario
items = mi_diccionario.items()

print("Tuplas (clave, valor) del diccionario:", items)

mi_diccionario = {"nombre": "Juan", "edad": 30}

# Obtener el valor asociado a la clave "nombre"
nombre = mi_diccionario.get("nombre")

# Obtener el valor asociado a la clave "ciudad" (que no existe)
ciudad = mi_diccionario.get("ciudad", "Ciudad desconocida")

print("Nombre:", nombre)
print("Ciudad:", ciudad)
