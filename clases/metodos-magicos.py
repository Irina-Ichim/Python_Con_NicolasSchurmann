""" metodos magicos _ se ejecutan cuando no los llamamos"""

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __del__(self):
        print(f"Chao perro :( {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

perro = Perro("Chanchito", 7)
del perro
# print(perro)
# texto = str(perro)
# print(texto)


# perro.__     Te muestra el listado de todos los metodos magicos
# Toda la información sobre los metodos magicos https://rszalski.github.io/magicmethods/
# El constructor es un metodo magico que se ejecuta cuando creamos un objeto
# El destructor es un metodo magico que se ejecuta cuando eliminamos un objeto