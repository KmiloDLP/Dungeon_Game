import math
from Class.Card_structures.Class.Cartas import Carta

class Golems(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Golem", Type, HP, MP, Atk, Def, Spd, auto_skills=True)

    def Recibir_daño(self, ataque, atacante=None):

        daño_real = math.ceil(ataque * 0.7)
        return super().Recibir_daño(daño_real)