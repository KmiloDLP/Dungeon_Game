import math
from Class.Card_structures.Class.Cartas import Carta

class Cristalize(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Cristalize", Type, HP, MP, Atk, Def, Spd, auto_skills=True)
        self.cargas = 0


    def Attack(self, daño, target):

        daño = int(daño * (1 + self.cargas * 0.2))
        result = target.Recibir_daño(daño, self)

        self.cargas = 0
        return result

    def Recibir_daño(self, ataque, atacante=None):
        self.cargas += 1
        self.anim_state = "hurt"
        self.anim_timer = 15

        super().Recibir_daño(ataque)

