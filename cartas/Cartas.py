from design.Marco import Marco

class Carta:
    def __init__(self, nombre, vida, atk):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.atk = atk

        rank_atk = self.calcular_rank_atk(self.atk)
        rank_hp = self.calcular_rank_hp(self.vida_max)

        self.marco = Marco(rank_hp, rank_atk, self.nombre)

    def Atacar(self, target):
        target.Recibir_daño(self.atk)

    def Recibir_daño(self, ataque):
        self.vida -= ataque

        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} ha recibido {ataque} de daño")

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "vida": self.vida,
            "vida_max": self.vida_max,
            "atk": self.atk
    }

    @staticmethod
    def calcular_rank_atk(atk):
        if atk >= 46:
            return "A"
        elif atk >= 38:
            return "B"
        elif atk >= 26:
            return "C"
        return "D"


    @staticmethod
    def calcular_rank_hp(vida):
        if vida >= 150:
            return "A"
        elif vida >= 100:
            return "B"
        elif vida >= 60:
            return "C"
        return "D"