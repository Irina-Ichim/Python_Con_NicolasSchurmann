from collections import deque

# Creamos una fila (cola) inicializada con los elementos 1 y 2.
fila = deque([1, 2])

# Vamos a realizar algunas operaciones sobre la fila.
# Descomentaremos las líneas para ver cómo funcionan.

# Añadimos elementos al final de la fila.
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)  # Esto imprimirá la fila con los elementos [1, 2, 3, 4, 5]

# Eliminamos el primer elemento de la fila (el 1 en este caso).
fila.popleft()
fila.popleft()

print(fila)  # Esto imprimirá la fila con los elementos [3, 4, 5]

# Comprobamos si la fila está vacía.
if not fila:
    print("Fila vacía")

print(fila)  # Esto volverá a imprimir la fila [3, 4, 5]

# En resumen biblioteca collections de Python para crear una fila (cola) con la característica FIFO (First-In, First-Out) utilizando deque. Sin embargo,
# la mayoría de las operaciones están comentadas en el código, por lo que se están omitiendo algunas acciones.
# Una fila, en el contexto de estructuras de datos, es una colección de elementos organizados según el principio FIFO (First-In, First-Out). 
# Esto significa que el primer elemento que se agrega a la fila es el primero en ser eliminado, y los elementos se manejan en el orden en el que se agregaron.
# Es similar a la forma en que las personas se alinean en una cola (fila) en la vida cotidiana: la primera persona que llega es la primera en ser atendida.

#En programación, las filas (también conocidas como colas) son útiles para realizar tareas en un orden específico. Puedes agregar elementos al final
# de la fila y eliminar elementos del frente de la fila. Estas estructuras de datos se utilizan comúnmente en situaciones donde es importante respetar
# el orden de llegada, como en la administración de tareas o la gestión de solicitudes en un servidor.