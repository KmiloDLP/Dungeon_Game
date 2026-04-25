
from cartas.Cartas import Carta


class Ogros(Carta):
    def __init__(self, vida, atk):
        super().__init__("Ogro", vida, atk)


def Atacar(self):
        vida_perdida = self.vida_max - self.vida
        ataque = self.atk + (vida_perdida * 0.1)
        
        return ataque