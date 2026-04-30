import math
from cartas.Cartas import Carta

class Golems(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd):
        super().__init__("Golem", Type, HP, MP, Atk, Def, Spd)

    def Recibir_daño(self, ataque):
        daño_real = math.ceil(ataque * 0.7)
        return super().Recibir_daño(daño_real)