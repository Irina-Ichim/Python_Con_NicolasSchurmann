"""
Este programa muestra ejemplos de diferentes operaciones y métodos de cadenas en Python.

1. Split y Join:
   - Divide la cadena 'texto' en una lista de palabras utilizando el método .split().
   - Une las palabras de la lista 'palabras' en una sola cadena con espacios como separadores utilizando el método .join().

2. Startswith:
   - Verifica si la cadena 'frase' comienza con las subcadenas "Hola" y "¿cómo" utilizando el método .startswith().

3. Count, Index, isalpha, isdigit, isalnum:
   - Cuenta las ocurrencias de "chocolate" en la cadena 'postres' usando .count().
   - Encuentra el índice de la subcadena "tarta" en 'postres' utilizando .index().
   - Comprueba si 'postres' consiste solo en caracteres alfabéticos, dígitos o alfanuméricos usando los métodos .isalpha(), .isdigit() y .isalnum().

4. Verificación personalizada:
   - Realiza una verificación personalizada en la cadena 'frase1' para determinar si cumple con ciertas condiciones.

5. Formateo con .format():
   - Utiliza el método .format() para formatear una cadena con valores variables, incluyendo 'nombre' y 'edad'.
"""




texto = "Esta es una muestra de texto para dividir."
print(texto.split())

# Lista de palabras
palabras = ["Hola", "este", "es", "un", "ejemplo"]

# Unir las palabras en una cadena usando un espacio en blanco como separador
frase = " ".join(palabras)

# Imprimir la cadena resultante
print(frase)

frase = "Hola, ¿cómo estás?"

# Verificar si la frase comienza con "Hola"
resultado = frase.startswith("Hola")

# Imprimir el resultado
print(resultado)
resultado = frase.startswith("¿cómo")
print(resultado)

postres = "bombones de chocolate, tarta de chocolate, helado de chocolate"

print(postres.count("chocolate"))
print(postres.index("tarta"))
print(postres.isalpha())
print(postres.isdigit())
print(postres.isalnum())

frase1 = "Hola, cómo estás?"

# Inicializamos una bandera como True
es_valido = True

# Recorremos cada carácter de la cadena
for caracter in frase1:
    # Verificamos si el carácter no es una letra ni una coma
    if not (caracter.isalpha() or caracter == ","):
        # Si encontramos un carácter que no cumple con la condición, cambiamos la bandera a False y salimos del bucle
        es_valido = False
        break

# Imprimimos el resultado
if es_valido:
    print("La cadena cumple con las condiciones.")
else:
    print("La cadena no cumple con las condiciones.")
    
nombre = "Juan"
edad = 30

# Usamos el método .format() para formatear una cadena con valores variables
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)

# Imprimir el mensaje formateado
print(mensaje)

