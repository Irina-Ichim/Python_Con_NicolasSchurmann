#override method
# metodo que hemos heredado y decidimos reemplazarlo por otro

class Ave:
    def __init__(self):
        self.volador = "volador"
        
    def vuela(self):
        print("vuela")
        
class Pato(Ave): # Anulamos el metodo de la clase padre
    def __init__(self):
        super().__init__()
        self.nada = "nadador"
    def vuela(self):
        super().vuela()
        print("vuela pato")
        
pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)

# la palabra reservada de super nos entrega acceso inmediato a todos los metodos y propiedades que tiene la clase padre           