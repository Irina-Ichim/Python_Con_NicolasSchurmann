punto = {"x": 25, "y": 50}
# los diccionarios usan { }, key debe ser string, el value puede ser cualquier cosa
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45  # crear una nueva llave dentro de mi diccionario

print(punto)
print(punto.get("lala", 97))  # utilizamos .get para agregar un nuevo valor a nuestro diccionario
del punto["z"]
print(punto)

# iterar
for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)
    
for llave, valor in punto.items():
    print(llave, valor)

# si trabajas con una base de datos necesitas un id    
usuarios = [
    {"id":1, "nombre":"Chanchito"},
     {"id":2, "nombre":"Feliz"},
      {"id":3, "nombre":"Nicolas"},
       {"id":4, "nombre":"Felipe"},
        {"id":5, "nombre":"Irina"},
]

# queremos acceder solamente a los nombres, iteramos los usuarios
for usuario in usuarios:
    print(usuario["nombre"])
