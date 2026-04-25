
from cartas.Cartas import Carta


class Fenixs(Carta):
    def __init__(self, vida, atk):
        super().__init__("Fenix", vida, atk)
        self.renacido = False

    def Recibir_daño(self, ataque):
        daño=ataque
        self.vida -= daño
        if self.vida <= 0:

            if not self.renacido:
                self.vida = self.vida_max * 0.5
                self.renacido = True
                print(f"{self.nombre} ha renacido con {self.vida} de vida")
            else:
                self.vida = 0
                print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} ha resibido {daño} de daño")

    def Atacar(self):
        ataque = self.atk
        if self.renacido:
            ataque *= 2
        
        return ataque