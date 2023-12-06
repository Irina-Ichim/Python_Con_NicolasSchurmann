from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass
    
class Usuario(Model):
    def guardar(self):
        print("guardadndo en BBDD")
        
class Sesion(Model):
    def  guardar(self):
        print("guardando en archivo")
        
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
    
usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])
        
# el polimorfismo en Python permite que diferentes clases compartan un método o atributo común, lo que mejora la flexibilidad y 
# la reutilización del código en aplicaciones orientadas a objetos.   