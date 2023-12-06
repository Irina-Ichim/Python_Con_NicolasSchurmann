class Model():
    tabla = False
    
    def __init__(self):
        if not self.tabla:
            print("tienes que definir una tabla")
            
    def guardar(self):
        print(f"Guardadndo { self.tabla} en BBDD")
        
    @classmethod    
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")
        
class Usuario(Model):
    tabla = "Usuario"
    
usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)

# utilizando herencia para compartir funcionalidades comunes en una clase base (Model) y luego extendiendo esa clase base para crear una clase derivada (Usuario) 
# que especifica su propia implementación para ciertos atributos y métodos. Este enfoque es típico en programación orientada a objetos y es una forma de reutilizar 
# y organizar el código.   
    