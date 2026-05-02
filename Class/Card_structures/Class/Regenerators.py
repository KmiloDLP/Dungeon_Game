
import math
from Class.Card_structures.Class.Cartas import Carta

class Regenerators(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Regenerator", Type, HP, MP, Atk, Def, Spd, auto_skills=True)

    def Recuperar_vida(self):
        heal = math.ceil(self.Base_HP * 0.1)
        self.HP = min(self.HP + heal, self.Base_HP)

        self.anim_state = "heal"
        self.anim_timer = 15

