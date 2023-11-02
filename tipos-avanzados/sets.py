# set significa grupo o conjunto
# usando los sets, python se encarga de eliminar los elementos duplicados
primer = {1, 1, 2, 2, 3, 4}

# los sets utilizan metodos parecidos a las listas: 
# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
# transformamos una lista a un set
segundo = set(segundo)
print(segundo)

# Operadores interesantes de sets
# print(primer | segundo)   union de los sets que le pasemos
# print (primer & segundo)  interseccion, devuelve los elementos en comun
# print(primer - segundo)   diferencia los datos diferentes que contiene la primera variable
print(primer ^ segundo)     # diferencia simetrica lo que tiene la primera variable y no tiene la segunda y tambien lo que tiene la segunda y no tiene la primera

