
from cartas.Cartas import Carta


class Dragones(Carta):
    def __init__(self, vida, atk):
        super().__init__("Dragon", vida, atk)
