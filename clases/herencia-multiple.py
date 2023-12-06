class Caminador:
    def caminar(self):
        print("cominando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Pato(Volador, Nadador, Caminador):     # Herencia multiple
    def programar(self):
        print("programando")
