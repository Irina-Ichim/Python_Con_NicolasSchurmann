# -*- coding: utf-8 -*-

class MiClase:
    """
    Esta es una clase de ejemplo para explicar atributos de clases,
    métodos de clases, cls y Factory Method.
    """

    # Atributo de clase compartido por todas las instancias
    atributo_de_clase = "Compartido por todas las instancias"

    def __init__(self, valor_instancia):
        """
        Constructor de la clase. Inicializa el atributo de instancia.

        Args:
            valor_instancia (any): Valor para el atributo de instancia.
        """
        self.atributo_de_instancia = valor_instancia

    @classmethod
    def metodo_de_clase(cls):
        """
        Método de clase asociado a la clase.

        Args:
            cls (type): Referencia a la clase.
        """
        print(f"Este es un método de clase asociado a la clase {cls}")

    def metodo_de_instancia(self):
        """
        Método de instancia asociado a la instancia.

        Utiliza self.__class__ para referirse a la clase.

        Args:
            self (MiClase): Referencia a la instancia.
        """
        print(f"Este es un método de instancia de la clase {self.__class__}")

    @staticmethod
    def factory_method(valor):
        """
        Factory Method estático que crea instancias de la clase.

        Args:
            valor (any): Valor para inicializar el atributo de la instancia.

        Returns:
            MiClase: Instancia creada por el Factory Method.
        """
        # Lógica de creación de la instancia
        if valor > 0:
            return MiClase(f"Valor positivo: {valor}")
        else:
            return MiClase(f"Valor no positivo: {valor}")


# Uso de la clase y sus métodos
MiClase.metodo_de_clase()

instancia = MiClase("Ejemplo")
instancia.metodo_de_instancia()

objeto_positivo = MiClase.factory_method(42)
objeto_no_positivo = MiClase.factory_method(-7)

print(objeto_positivo.atributo_de_instancia)
print(objeto_no_positivo.atributo_de_instancia)
