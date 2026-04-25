
from cartas.Cartas import Carta


class Dragones(Carta):
    def __init__(self, vida, atk):
        super().__init__("Dragon", vida, atk)

    def Recibir_daño(self, ataque, target):

        daño = ataque
        self.vida -= daño
        
        target.vida -= daño * 0.1
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} ha resibido {daño} de daño")
