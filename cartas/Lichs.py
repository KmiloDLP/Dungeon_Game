
from cartas.Cartas import Carta


class Lichs(Carta):
    def __init__(self, vida, atk):
        super().__init__(
            "Lich",
            int(vida * 0.5),
            int(atk * 2)
        )