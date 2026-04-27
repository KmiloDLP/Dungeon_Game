
from cartas.Cartas import Carta
from design.Marco import Marco



class Lichs(Carta):
    def __init__(self, vida, atk):
        super().__init__(
            "Lich",
            int(vida * 0.5),
            int(atk * 2)
        )
        rank_atk = self.calcular_rank_atk(atk)
        rank_hp = self.calcular_rank_hp(vida)

        self.marco = Marco(rank_hp, rank_atk, self.nombre)