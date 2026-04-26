import math
from cartas.Cartas import Carta


class Ogros(Carta):
    def __init__(self, vida, atk):
        super().__init__("Ogro", vida, atk)

    def Atacar(self):
        daño_extra = (self.vida_max - self.vida) * 0.1
        ataque = self.atk + daño_extra

        return math.ceil(ataque)