# and, or , not evaluan en true o false
# si usamos and , ambos valores deben ser true
# si usamos or , una de las condiciones debe ser true
# los operadores logicos los puedes utilizar dentro de los if
#gas = True

# gas = False
# encendido = True

# if gas and encendido:
#     print("Puedes avanzar")
# else:
#     print("Para en la gasolinera")

# if gas or encendido:
#     print("Puedes avanzar")

# if not gas and encendido:
#     print("Puedes avanzar")

# gas = True
# encendido = True
# edad = 18

# if gas and encendido and edad > 17:
#     print("Puedes avanzar")
    
    
# gas = True
# encendido = True
# edad = 18

# if gas and (encendido or edad > 17):   # Se evalua primero siempre los parantesis
#     print("Puedes avanzar")
    
    
gas = False
encendido = True
edad = 18

if not gas and (encendido or edad > 17):   # Se evalua primero siempre los parantesis
    print("Puedes avanzar")