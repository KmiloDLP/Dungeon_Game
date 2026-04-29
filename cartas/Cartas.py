import math
from re import match

from design.Marco import Marco

class Carta:

    def __init__(self, nombre, vida, atk):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.atk = atk
        self.atk_origin= atk


        self.anim_state = "idle"
        self.anim_timer = 0
        self.shake = 0

        rank_atk = self.calcular_rank_atk(self.atk)
        rank_hp = self.calcular_rank_hp(self.vida_max)

        self.marco = Marco(rank_hp, rank_atk, self.nombre)

    def Atacar(self):
        daño = self.atk
        return math.ceil(daño)

    def Recibir_daño(self, ataque):
        self.vida -= ataque

        self.anim_state = "hurt"
        self.anim_timer = 15
        self.shake = 8

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

    def Pocion_Use(self, Pocion):

        porcentaje = 0
        match Pocion:
            case "Minipocion":
                porcentaje = 0.1
            case "Pocion":
                porcentaje = 0.3
            case "Superpocion":
                porcentaje = 0.5
            case "Hiperpocion":
                porcentaje = 1.0

        curacion = int(self.vida_max * porcentaje)
        if self.vida + curacion > self.vida_max:
            curacion = self.vida_max - self.vida
        self.vida = min(self.vida + curacion, self.vida_max)
        return curacion
    
    def victori(self):
        self.vida = self.vida_max
        self.atk = self.atk_origin

    def obtener_rango_venta(self):
        """Obtiene el rango de venta basado en ATK y HP (el más alto)"""
        rank_atk = self.calcular_rank_atk(self.atk)
        rank_hp = self.calcular_rank_hp(self.vida_max)
        
        # Comparar y retornar el rango más alto
        rangos_valor = {"A": 4, "B": 3, "C": 2, "D": 1}
        return max([rank_atk, rank_hp], key=lambda r: rangos_valor[r])
    
    def obtener_valor_venta(self):
        """Retorna el valor en oro según el rango"""
        rango = self.obtener_rango_venta()
        valores = {
            "A": 100,
            "B": 50,
            "C": 30,
            "D": 20
        }
        return valores.get(rango, 20)

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