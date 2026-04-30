import math
from cartas.Cartas import Carta

class Cristalize(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd):
        super().__init__("Cristalize", Type, HP, MP, Atk, Def, Spd)
        self.cargas = 0

    def Atacar(self):
        ataque = self.Atk * (1 + 0.25 * self.cargas)
        self.cargas = 0
        return math.ceil(ataque)

    def Recibir_daño(self, ataque):
        self.cargas += 1
        self.anim_state = "heal"
        self.anim_timer = 15

        super().Recibir_daño(ataque)
        return "Charged"

