import math
from cartas.Cartas import Carta

class Drains(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd):
        super().__init__("Drain", Type, HP, MP, Atk, Def, Spd)

    def Atacar(self):
        daño = math.ceil(self.Atk)
        self.HP = min(self.HP + math.ceil(daño * 0.1), self.Base_HP)
        return daño

    def Recuperar_vida(self, daño):
        heal = math.ceil(daño * 0.25)
        self.HP = min(self.HP + heal, self.Base_HP)

        self.anim_state = "heal"
        self.anim_timer = 15