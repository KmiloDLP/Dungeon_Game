import math
from Class.Card_structures.Class.Cartas import Carta

class Cristalize(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Cristalize", Type, HP, MP, Atk, Def, Spd, auto_skills=True)
        self.cargas = 0

    def Atacar(self, objetivo):
        ataque = self.Atk * (1 + 0.25 * self.cargas)
        self.cargas = 0
        damage = objetivo.Recibir_daño(ataque)
        return damage

    def Recibir_daño(self, ataque, atacante=None):
        self.cargas += 1
        self.anim_state = "hurt"
        self.anim_timer = 15

        super().Recibir_daño(ataque)

