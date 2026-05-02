import math
from Class.Card_structures.Class.Cartas import Carta

class Drains(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Drain", Type, HP, MP, Atk, Def, Spd, auto_skills=True)

    def Atacar(self, objetivo):
        daño = math.ceil(self.Atk)
        self.HP = min(self.HP + math.ceil(daño * 0.1), self.Base_HP)
        objetivo.Recibir_daño(daño, self)
