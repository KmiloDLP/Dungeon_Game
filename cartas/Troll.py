
from cartas.Cartas import Carta


class Trolls(Carta):
    def __init__(self, vida, atk):
        super().__init__("Troll", vida, atk)

    def Recuperar_vida(self):
        vida_recuperada = self.vida_max * 0.1
        self.vida += vida_recuperada
        if self.vida > self.vida_max:
            self.vida = self.vida_max
        print(f"{self.nombre} ha recuperado {vida_recuperada} de vida")