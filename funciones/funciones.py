def hola(nombre, apellido):
    print("Hola Mundo")
    print(f"Bienvenida {nombre} {apellido}")   # nombre es parametro


hola("Irina", "Irina")      # estoy llamando a la funcion / Irina es un valor y por lo tanto un argumento
hola("Chanchito" ,"Feliz")

# Pasamos parametros por defecto

def persona(nombre, ciudad="Barcelona"):
    print("Hola Mundo")
    print(f"Bienvenida {nombre} {ciudad}")
    
    
persona("irina", "ichim")
persona("chanchito")

# argumentos nombrados
hola(apellido="ichim", nombre="irina")  