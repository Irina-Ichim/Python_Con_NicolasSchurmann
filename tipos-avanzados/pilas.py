pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimoElemnto = pila.pop() # elimina el ultimo elemento de la pilla
print(ultimoElemnto)

#para acceder a ultimo elemeto de una lista recuerda utilizar el indice de -1

print(pila[-1])
pila.pop()
pila.pop()

# para validar usa if not
if not pila:
    print("pila vacia")
    
# En resumen, En Python, una pila es otra estructura de datos que almacena elementos, pero sigue un principio diferente al de una fila. En una pila, los elementos
# se organizan según el principio LIFO (Last-In, First-Out), lo que significa que el último elemento agregado es el primero en ser eliminado.
# Es similar a una pila de platos: el último plato que se coloca en la pila es el primero que se retira.

# En una pila, solo puedes agregar elementos en la parte superior (apilar) y eliminar elementos de la parte superior (desapilar). No puedes acceder ni modificar
# elementos en el medio de la pila sin desapilar los elementos superiores. Las pilas son útiles en situaciones en las que necesitas realizar seguimiento de elementos
# en orden inverso, como al evaluar expresiones matemáticas o al realizar operaciones de retroceso en editores de texto.

#Python proporciona una estructura de datos llamada "stack" (pila) que se puede implementar utilizando listas. Puedes agregar elementos a la pila usando el 
# método append() y eliminar elementos de la pila usando el método pop().    