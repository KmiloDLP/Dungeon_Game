import math
from cartas.Cartas import Carta


class Ogros(Carta):
    def __init__(self, vida, atk):
        super().__init__("Ogro", vida, atk)


    def Recibir_daño(self, ataque):

        self.vida -= ataque
        daño_extra = (self.vida_max - self.vida) * 0.1
        self.atk += math.ceil(daño_extra)

        self.anim_state = "hurt"
        self.anim_timer = 15
        self.shake = 8

        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} ha recibido {ataque} de daño")