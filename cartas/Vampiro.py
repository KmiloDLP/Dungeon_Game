
from cartas.Cartas import Carta


class Vampiros(Carta):
    def __init__(self, vida, atk):
        super().__init__("Vampiro", vida, atk)

    def Atacar(self):
        ataque = self.atk
        self.vida += ataque * 0.1
        return ataque
