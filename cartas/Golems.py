import math

from cartas.Cartas import Carta

class Golems(Carta):
    def __init__(self, vida, atk):
        super().__init__("Golem", vida, atk)

    def Recibir_daño(self, ataque):
        daño_real = ataque * 0.7 

        self.vida -= math.ceil(daño_real)

        self.anim_state = "hurt"
        self.anim_timer = 15
        self.shake = 8

        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} ha recibido {math.ceil(daño_real)} de daño")