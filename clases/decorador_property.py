# class Perro:
#     def __init__(self,nombre):        #constructor
#         self.nombre = nombre
        
#     def set_nombre(self, nombre):
#         if nombre.strip():
#             self.__nombre = nombre
#         return  
    
#     def  get_nombre(self):
#         return self.__nombre     
        
# perro = Perro("King") 
# #print(perro)       # nos imprime <__main__.Perro object at 0x000002A775EAEAD0> clase main, objeto y espacio en memoria

# # nos va imprimir lo mismo si utilizamos un string vacio o un boolean, como prevenimos esto?
# print(perro.get_nombre)


# Lo hacemos de una manera más elegante
class Perro:
    def __init__(self,nombre):        
        self.nombre = nombre
     
    @property                     # le decimos al metodo que lo transforme en una propiedad, property se utiliza solamente con las funciones que nos van a devolver el valor
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre       
    
    @nombre.setter    
    def nombre(self, nombre):
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return  
    
perro = Perro("King")
print(perro.nombre)

class Circulo:
    def __init__(self, radio):
        self._radio = radio  # Atributo privado

    @property
    def radio(self):
        """Método getter para obtener el radio."""
        return self._radio

    @radio.setter
    def radio(self, valor):
        """Método setter para establecer el radio."""
        if valor > 0:
            self._radio = valor
        else:
            print("Error: El radio debe ser mayor que 0.")

# Uso de la clase
mi_circulo = Circulo(5)

# Accede al método getter
print("Radio inicial:", mi_circulo.radio)

# Utiliza el método setter
mi_circulo.radio = 7
print("Nuevo radio:", mi_circulo.radio)

# Intenta establecer un radio inválido
mi_circulo.radio = -3  # Esto mostrará un mensaje de error
