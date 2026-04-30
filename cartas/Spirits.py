import random
from cartas.Cartas import Carta


class Spirits(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd):
        super().__init__("Spirit", Type, HP, MP, Atk, Def, Spd)

    def Recibir_daño(self, ataque):

        dado = random.randint(0, 9)

        if dado in (0, 9):
            print(f"{self.nombre} esquivó el ataque!")
            return "miss" 

        super().Recibir_daño(ataque)
        return "hit"