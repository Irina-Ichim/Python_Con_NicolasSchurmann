# Archivo: duck_typing_example.py

class Pato:
    def hacer_sonido(self):
        """Produce el sonido característico de un pato."""
        return "Quack"

class Persona:
    def hacer_sonido(self):
        """Imita el sonido de un pato desde una perspectiva humana."""
        return "Habla como un pato"

def hacer_cua(cosa_que_hace_cua):
    """
    Hace que una cosa que hace cua emita su sonido característico.

    Parameters:
    - cosa_que_hace_cua: Un objeto que tiene un método hacer_sonido.

    Returns:
    - El resultado del método hacer_sonido de la cosa que hace cua.
    """
    return cosa_que_hace_cua.hacer_sonido()

# Creamos instancias de las clases Pato y Persona
pato = Pato()
persona = Persona()

# Llamamos a la función hacer_cua con objetos de diferentes clases
resultado_pato = hacer_cua(pato)
resultado_persona = hacer_cua(persona)

# Mostramos los resultados
print("El pato hace:", resultado_pato)  # Salida: El pato hace: Quack
print("La persona hace:", resultado_persona)  # Salida: La persona hace: Habla como un pato
