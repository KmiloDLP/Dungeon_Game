import math
from Class.Card_structures.Class.Cartas import Carta

class Drains(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Drain", Type, HP, MP, Atk, Def, Spd, auto_skills=True)

    def Attack(self, daño, target):

        heal = int(daño * 0.5)
        self.Heal(heal)
        super().Attack(daño, target)