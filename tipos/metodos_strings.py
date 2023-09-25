"""
Este programa demuestra varios métodos de manipulación de cadenas en Python.
"""

# Manipulación de cadenas con el nombre 'animal'
animal = "chanchito feliz"

# Convertir la cadena a mayúsculas
print(animal.upper())

# Convertir la cadena a minúsculas
print(animal.lower())

# Capitalizar la cadena (primera letra en mayúscula)
print(animal.capitalize())

# Capitalizar todas las palabras en la cadena
print(animal.title())

# Manipulación de cadenas con el nombre 'flor'
flor = "  rosa  amarilla "

# Eliminar espacios en blanco al principio y capitalizar
print(flor.strip().capitalize())

# Eliminar espacios en blanco al principio y al final
print(flor.strip())

# Eliminar espacios en blanco al final
print(flor.rstrip())

# Eliminar espacios en blanco al principio
print(flor.lstrip())

# Manipulación de cadenas con el nombre 'name'
name = "Karina"

# Encontrar la subcadena "ri" en 'name'
print(name.find("ri"))

# Encontrar la subcadena "Ki" en 'name'
print(name.find("Ki"))

# Reemplazar "Ka" por "I" en 'name'
print(name.replace("Ka", "I"))

# Verificar si "Ka" está en 'name'
print("Ka" in name)

# Verificar si "Ka" no está en 'name'
print("Ka" not in name)

animal = "chanchito feliz"
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())

flor = "  rosa  amarilla "
print(flor.strip().capitalize())
print(flor.strip())
print(flor.rstrip())
print(flor.lstrip())

name = "Karina"
print(name.find("ri"))
print(name.find("Ki"))
print(name.replace("Ka" , "I" ))
print("Ka" in name)
print("Ka" not in name)