class MiClase:
    def __init__(self, valor):
        self.__propiedad_privada = valor

    # Método getter para acceder a la propiedad privada
    def get_propiedad_privada(self):
        return self.__propiedad_privada

    # Método setter para modificar la propiedad privada
    def set_propiedad_privada(self, nuevo_valor):
        self.__propiedad_privada = nuevo_valor

# Crear una instancia de la clase
mi_instancia = MiClase(42)

# Acceder a la propiedad privada utilizando el método getter
valor_actual = mi_instancia.get_propiedad_privada()
print(f"Valor actual de propiedad privada: {valor_actual}")

# Modificar la propiedad privada utilizando el método setter
mi_instancia.set_propiedad_privada(99)
print(f"Nuevo valor de propiedad privada: {mi_instancia.get_propiedad_privada()}")

# Intentar acceder directamente a la propiedad privada (no se recomienda)
# Esto imprimirá el valor, pero no se debe hacer en la práctica
print(f"Acceso directo a propiedad privada: {mi_instancia._MiClase__propiedad_privada}")

# Acceder al diccionario __dict__ para ver todas las propiedades (no se recomienda)
# Esto imprimirá un diccionario con todas las propiedades, incluidas las privadas
print(f"Todas las propiedades: {mi_instancia.__dict__}")

#En Python, una propiedad privada es una variable o atributo de una clase que está destinado a ser utilizado solo internamente dentro de 
# la propia clase. La convención en Python para indicar que un atributo es privado es agregar un doble guion bajo (__) como prefijo al 
# nombre del atributo.