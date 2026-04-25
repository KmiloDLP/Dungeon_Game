
from random import random

from cartas.Cartas import Carta
    

class Fantasmas(Carta):
    def __init__(self, vida, atk):
        super().__init__("Fantasma", vida, atk)

    def Recibir_daño(self, ataque):
        daño=ataque

        dado = random.randint(0, 9)

        if dado == 0 or dado == 9:  
            print(f"{self.nombre} no ha recibido daño")
        else:
            self.vida -= daño
            if self.vida <= 0:
                self.vida = 0
                print(f"{self.nombre} ha sido derrotado")
            else:
                print(f"{self.nombre} ha resibido {daño} de daño")
