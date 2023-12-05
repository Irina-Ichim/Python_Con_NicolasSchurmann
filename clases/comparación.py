class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
    def __eq__(self, otrainstancia):    #equal
        return self.lat == otrainstancia.lat and self.lon == otrainstancia.lon
    
    # Python ya sabe que hacer cuando definimos este metodo    
    # def __ne__(self, otro):
    #     return self.lat != otro.lat or self.lon != otro.lon # not equal
    def __lt__(self, otro):      # lt significa menor que
        return self.lat + self.lon < otro.lat + otro .lon   
    
    def __le__(self, otro):    # le significa menor o igual
         return self.lat + self.lon <= otro.lat + otro .lon
     
coords = Coordenadas(45, 37)
coords2 = Coordenadas(45, 37)

# print(coords == coords2)
# print(coords, coords2)
# print(coords != coords2)
print(coords <= coords2)
# <__main__.Coordenadas object at 0x00000284D72EFFD0> <__main__.Coordenadas object at 0x00000284D72F0050> , 0x00000284D72EFFD0  representa espacio en memoria, los ultimos dos numeros representa donde los almacena
