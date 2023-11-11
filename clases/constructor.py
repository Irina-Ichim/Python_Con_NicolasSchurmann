class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):
        print(f"{self.nombre} dice: Guau!")
        
mi_perro = Perro("Chanchito", 1)
mi_perro.habla()
#mi_perro2 = Perro("Felipe")
# print(mi_perro.nombre)
# print(mi_perro2.nombre)

# __init__(self, nombre, edad): Este es un método especial llamado constructor. Se llama automáticamente cuando creas una nueva instancia de la clase. self es el primer
# parámetro y se refiere a la instancia actual. nombre y edad son parámetros que se utilizan para inicializar los atributos de la instancia.
#self.nombre y self.edad: Estos son atributos de la instancia. self se utiliza para referirse a la instancia actual, y puedes pensar en estos atributos como variables 
# asociadas a cada instancia de la clase.

#habla(self): Este es un método de la clase Perro. Al igual que con el constructor, self es el primer parámetro, permitiendo que el método acceda a los atributos y 
# otros métodos de la instancia.

#mi_perro = Perro("Chanchito", 1): Aquí se crea una instancia de la clase Perro llamada mi_perro con el nombre "Chanchito" y la edad 1.

#mi_perro.habla(): Se llama al método habla en la instancia mi_perro, lo que imprime un mensaje que incluye el nombre del perro.
