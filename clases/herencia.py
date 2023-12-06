class Animal:
    def comer(self):
        print("comiendo")

class Perro(Animal):
    def pasear(self):
        print("paseando")
        

class Chanchito(Perro):
   def programar(self):
        print("programando")
        
chanchito = Chanchito()
# chanchito.  Herencia de multinivel, trata de no hacerlo más de 2 veces