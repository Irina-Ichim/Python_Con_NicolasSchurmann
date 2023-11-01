# Las listas, los strings, los resultados de la funcion range son iterables
# Para iterar usa el for

mascotas = [ "King", "Chuchy", "Pelusa", "Pulga"]

for indice, mascota in enumerate(mascotas):   # enumerate devuelve un listado de tuplas, primero es el indice, segundo el nombre
    print(indice, mascota)