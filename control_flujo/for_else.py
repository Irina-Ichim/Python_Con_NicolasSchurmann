# buscar = 3
buscar = 13
for numero in range(5):
   print(numero)            # devuelve 0,1,2,3,4
   if numero == buscar:
       print("encontrado", buscar)
       break
else:
    print("No encontre el numero buscado :(")   