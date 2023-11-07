lista1 = [1, 2, 3, 4]
print(*lista1)  # para desenpaquetar cualquier iterable

# podemos hacer lo mismo con las tuplas
listaUno = (1, 2, 3, 4)
print(*listaUno)

# combinar listas
lista2 = [5, 6]

# combinada = [*lista1, *lista2]
# print(combinada)

#entre medio puedo agregar lo que necesitas
combinada = ["Hola", *lista1,"mundo", *lista2, "chanchito"]
print(combinada)

# para diccionarios sera **
punto1 = {"x": 1, "y": 2}
punto2 = {"z": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)

#si queremos agregar mas propiedades a nuestro nuevo diccionario nuevoPunto, lo puedes hacer de la siguiente manera

nuevoPunto1 = {**punto1, "lalala": "Hola Mundo", **punto2, "z": 10, "p": "Me gusta el Python"}
print(nuevoPunto1)
    