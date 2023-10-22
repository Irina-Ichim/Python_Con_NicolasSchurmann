# Si quiero pasar multiples argumentos a mi funcion

# def suma(a, b, c):
#     print(a+ b + c)
    
    
# suma(2, 5, 7)

#xargs herramienta que permite tomar una lista de elementos
#desde la entrada estandar y ejecutar un comando en cada uno de los elementos
def suma(*numeros):  # los parametros lo transforma en iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)        
    
suma(2, 5, 7)
suma(3, 9) 
suma(2, 8, 7, 45, 32)   
    
