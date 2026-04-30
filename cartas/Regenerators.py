
import math
from cartas.Cartas import Carta

class Regenerators(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd):
        super().__init__("Regenerator", Type, HP, MP, Atk, Def, Spd)

    def Recuperar_vida(self):
        heal = math.ceil(self.Base_HP * 0.1)
        self.HP = min(self.HP + heal, self.Base_HP)

        self.anim_state = "heal"
        self.anim_timer = 15

        print(f"{self.nombre} recupera {heal}")