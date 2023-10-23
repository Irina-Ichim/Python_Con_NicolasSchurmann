# def saludar():
#     saludo = "Hola Mundo"
#     print(saludo)
    
# def saludaChanchito():
#     saludo = "Hola Chanchito"   # variables con valores distintos
#     print(saludo)
    
# saludar()
# saludaChanchito() 
# saludar()   


# Lo mismo pero definiedo la variable fuera como contexto global

saludo = "Hola global"
def saludar():
    saludo = "Hola Mundo"

    
def saludaChanchito():
     saludo = "Hola Chanchito"   # variables con valores distintos
     print(saludo)
    
saludar()
print(saludo)
  
# Es mala practica usar variables globales  