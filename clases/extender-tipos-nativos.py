# lista = list([1, 2, 3])

# lista.append(4)
# lista.insert(0, 0)

# print(lista)

# para hacer el codigo mas intuitivo
class Lista(list):
    def prepend(self, item):       #agrega los elementos a inicio
        self.insert(0, item)
        
lista = Lista([1,2,3])
lista.append(4)
lista.prepend(0)

print(lista)
