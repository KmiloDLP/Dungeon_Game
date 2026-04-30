import math
from cartas.Cartas import Carta

class Warriors(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd):
        super().__init__("Warrior", Type, HP, MP, Atk, Def, Spd)

    def Recibir_daño(self, ataque):
        resultado = super().Recibir_daño(ataque)

        daño_perdido = self.Base_HP - self.HP
        bonus = math.ceil(daño_perdido * 0.1)
        self.Atk = self.Base_Atk + bonus

        return resultado