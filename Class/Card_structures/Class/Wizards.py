from Class.Card_structures.Class.Cartas import Carta

class Wizards(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Wizard",Type,int(HP * 0.5),MP,int(Atk * 2),Def,Spd, auto_skills=True)