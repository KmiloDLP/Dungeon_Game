import math
import random
from design.Marco import Marco


class Carta:

    def __init__(self, Class, Type, HP, MP, Atk, Def, Spd):

 
        self.Class = Class
        self.Type = Type

        self.Base_HP = HP
        self.Base_Atk = Atk
        self.Base_Def = Def
        self.Base_Spd = Spd
        self.Base_MP = MP

        self.HP = self.Base_HP
        self.MP = self.Base_MP
        self.Atk = self.Base_Atk
        self.Def = self.Base_Def
        self.Spd = self.Base_Spd


        self.anim_state = "idle"
        self.anim_timer = 0
        self.shake = 0


        self.Characteristics = Marco(
            self.Class,
            self.Type,
            self.Base_HP,
            self.Base_Def,
            self.Base_Atk,
            self.Base_Spd,
            self.Base_MP
        )


    def Atacar(self):
        return math.ceil(self.Atk)

    def Recibir_daño(self, ataque):

        damage = ataque - (ataque * (self.Def / 100))
        damage = max(1, int(damage))  # evitar daño 0

        self.HP -= damage

        # animación
        self.anim_state = "hurt"
        self.anim_timer = 15
        self.shake = 8

        if self.HP <= 0:
            self.HP = 0
            return "dead"

        return damage


    def Pocion_Use(self, pocion):

        porcentajes = {
            "Minipocion": 0.1,
            "Pocion": 0.3,
            "Superpocion": 0.5,
            "Hiperpocion": 1.0
        }

        if pocion not in porcentajes:
            return 0

        porcentaje = porcentajes[pocion]

        curacion = int(self.Base_HP * porcentaje)
        curacion_real = min(curacion, self.Base_HP - self.HP)

        self.HP += curacion_real

        # animación heal
        self.anim_state = "heal"
        self.anim_timer = 10

        return curacion_real


    def victoria(self):
        self.HP = self.Base_HP
        self.Atk = self.Base_Atk


    def obtener_valor_venta(self):

        # usamos el rank ya calculado en el marco
        rango = self.marco.rank

        valores = {
            "S": 200,
            "A": 100,
            "B": 60,
            "C": 30,
            "D": 15
        }

        return valores.get(rango, 10)


    def to_dict(self):
        return {
            "Class": self.Class,
            "Type": self.Type,
            "Base_HP": self.Base_HP,
            "Base_Atk": self.Base_Atk,
            "Base_Def": self.Base_Def,
            "Base_Spd": self.Base_Spd,
            "Base_MP": self.Base_MP,
        }