""" metodos magicos _ se ejecutan cuando no los llamamos"""

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

perro = Perro("Chanchito", 7)
print(perro)
texto = str(perro)
print(texto)


# perro.__     Te muestra el listado de todos los metodos magicos
# Toda la información sobre los metodos magicos https://rszalski.github.io/magicmethods/