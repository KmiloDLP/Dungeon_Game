import math

from cartas.Cartas import Carta

class Cristalize(Carta):
    def __init__(self, vida, atk):
        super().__init__("Cristalize", vida, atk)
        self.cargas = 0

    def Atacar(self):
        ataque = self.atk
        for _ in range(self.cargas):
            ataque += self.atk * 1.5

        self.cargas = 0
        return math.ceil(ataque)

    def Recibir_daño(self, ataque):
        self.cargas += 1
        print(f"{self.nombre} gana una carga")

        super().Recibir_daño(ataque)

