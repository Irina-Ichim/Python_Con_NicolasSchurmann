# Clase que ilustra propiedades de clase y de instancia
class MiClase:
    # Atributo de clase compartido por todas las instancias
    atributo_de_clase = "Compartido por todas las instancias"

    def __init__(self, valor_instancia):
        # Atributo de instancia específico para cada instancia
        self.atributo_de_instancia = valor_instancia

# Accediendo al atributo de clase a través de la clase
print("Atributo de clase a través de la clase:", MiClase.atributo_de_clase)

# Creando instancias
instancia1 = MiClase("Valor para Instancia 1")
instancia2 = MiClase("Valor para Instancia 2")

# Accediendo al atributo de clase a través de una instancia
print("Atributo de clase a través de instancia1:", instancia1.atributo_de_clase)
print("Atributo de clase a través de instancia2:", instancia2.atributo_de_clase)

# Cambiando el valor del atributo de clase a través de la clase
MiClase.atributo_de_clase = "Nuevo valor compartido"

# Accediendo al atributo de clase después del cambio
print("Atributo de clase después del cambio (instancia1):", instancia1.atributo_de_clase)
print("Atributo de clase después del cambio (instancia2):", instancia2.atributo_de_clase)

# Cambiando el valor del atributo de instancia solo para una instancia
instancia1.atributo_de_instancia = "Nuevo valor para Instancia 1"

# Accediendo a los atributos de instancia
print("Atributo de instancia (instancia1):", instancia1.atributo_de_instancia)
# La siguiente línea generará un error ya que instancia2 no tiene este atributo
# print("Atributo de instancia (instancia2):", instancia2.atributo_de_instancia)


#En Python, las propiedades de clases son atributos que están asociados con la clase en lugar de con instancias específicas de la clase.
# Hay dos tipos de atributos en Python: atributos de clase y atributos de instancia.

# 1.Atributos de Clase:
# Son compartidos por todas las instancias de la clase.
# Si cambias el valor de un atributo de clase, el cambio se reflejará en todas las instancias de esa clase.
# Se definen fuera de cualquier método de la clase y se comparten entre todas las instancias.

# 2.Atributos de Instancia:
# Son específicos de cada instancia de la clase.
# Cada instancia puede tener un valor diferente para estos atributos.
# Se definen dentro de los métodos de la clase utilizando self.