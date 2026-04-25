import random
from cartas.Cartas import Carta

class Fantasmas(Carta):
    def __init__(self, vida, atk):
        super().__init__("Fantasma", vida, atk)

    def Recibir_daño(self, ataque):
        # 20% de evasión
        if random.randint(0, 9) in (0, 9):
            print(f"{self.nombre} esquivó el ataque!")
            return

        super().Recibir_daño(ataque)