
import math

from cartas.Cartas import Carta


class Vampiros(Carta):
    def __init__(self, vida, atk):
        super().__init__("Vampiro", vida, atk)

    def Atacar(self):
        ataque = self.atk
        self.vida += math.ceil(ataque * 0.1)
        return math.ceil(ataque)

    def Recuperar_vida(self, daño):
        vida_recuperada = daño * 0.25
        self.vida += math.ceil(vida_recuperada)

        self.anim_state = "heal"
        self.anim_timer = 15