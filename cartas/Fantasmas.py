import random
from cartas.Cartas import Carta


class Fantasmas(Carta):
    def __init__(self, vida, atk):
        super().__init__("Fantasma", vida, atk)

    def Recibir_daño(self, ataque):

        dado = random.randint(0, 9)

        if dado in (0, 9):
            print(f"{self.nombre} esquivó el ataque!")
            return "miss" 

        super().Recibir_daño(ataque)
        return "hit"