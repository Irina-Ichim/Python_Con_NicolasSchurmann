usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],
    
]

# nombres = []
# for usuario in usuarios:
#         nombres.append(usuario[0])
# print(nombres)

# Forma más elegante
# nombres = [usuario[0] for usuario in usuarios]   # usuario[0] le hemos aplicado una transformacion

# filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

#filtrar y transformar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)