from Class.Card_structures.Class.Cartas import Carta

class Dragons(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Dragon", Type, HP, MP, Atk, Def, Spd, auto_skills=True)

    def Recibir_daño(self, ataque, Objetivo=None):


        damage = ataque - (ataque * (self.Def / 100))
        damage = max(1, int(damage))  

        self.HP -= damage
        Objetivo.Recibir_daño(damage*0.1)

        self.anim_state = "hurt"
        self.anim_timer = 15
        self.shake = 8

        if self.HP <= 0:
            self.HP = 0
            return "dead"

        return damage
