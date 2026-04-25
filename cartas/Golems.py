from cartas.Cartas import Carta

class Golems(Carta):
    def __init__(self, vida, atk):
        super().__init__("Golem", vida, atk)

    def Recibir_daño(self, ataque):
        daño_real = ataque * 0.9  # reduce 10%

        self.vida -= daño_real

        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} ha recibido {daño_real} de daño")