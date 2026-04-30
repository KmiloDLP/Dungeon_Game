from cartas.Cartas import Carta

class Dragons(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd):
        super().__init__("Dragon", Type, HP, MP, Atk, Def, Spd)