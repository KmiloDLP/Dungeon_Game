from Class.Card_structures.Class.Cartas import Carta

class Immortals(Carta):
    def __init__(self, Type, HP, MP, Atk, Def, Spd, auto_skills=True):
        super().__init__("Immortal", Type, HP, MP, Atk, Def, Spd, auto_skills=True)
        self.renacido = False

    def Recibir_daño(self, ataque):
        resultado = super().Recibir_daño(ataque)

        if self.HP <= 0 and not self.renacido:
            self.HP = int(self.Base_HP * 0.5)
            self.Atk = int(self.Base_Atk * 0.3)

            self.renacido = True
            self.anim_state = "heal"

            print(f"{self.nombre} ha renacido")
            return "revive"

        return resultado

