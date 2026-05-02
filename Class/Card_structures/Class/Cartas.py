import math
from Class.Utilities.Marco import Marco


class Carta:

    def __init__(self, Class, Type, HP, MP, Atk, Def, Spd, auto_skills=True):

        self.Class = Class
        self.Type = Type

        # Stats base
        self.Base_HP = HP
        self.Base_Atk = Atk
        self.Base_Def = Def
        self.Base_Spd = Spd
        self.Base_MP = MP

        # Stats actuales
        self.HP = self.Base_HP
        self.MP = self.Base_MP
        self.Atk = self.Base_Atk
        self.Def = self.Base_Def
        self.Spd = self.Base_Spd

        # Animaciones
        self.anim_state = "idle"
        self.anim_timer = 0
        self.shake = 0

        # Estados
        self.Debuff = "Normal"
        self.duration_debuff = 0

        self.Buff = "Normal"
        self.duration_buff = 0

        # 🔥 HABILIDADES
        self.habilidades = []
        if auto_skills:
            self.assign_skills()

        # Características visuales
        self.Characteristics = Marco(
            self.Class,
            self.Type,
            self.Base_HP,
            self.Base_Def,
            self.Base_Atk,
            self.Base_Spd,
            self.Base_MP
        )

    #ASIGNACION DE HABILIDADES
    def assign_skills(self):

        import random
        from ..Skills.Skills_registry import SKILLS_BY_TYPE, SKILLS_PHYSICAL

        skill_fisica = random.choice(SKILLS_PHYSICAL)
        skill_elemental = random.choice(SKILLS_BY_TYPE[self.Type])

        self.habilidades = [skill_fisica, skill_elemental]

    #  USO DE HABILIDADES
    def usar_habilidad(self, index, target=None):

        if index >= len(self.habilidades):
            return {"error": "habilidad_invalida"}

        habilidad = self.habilidades[index]

        try:
            resultado = habilidad.usar(self, target)
        except Exception as e:
            return {"error": str(e)}

        return {
            "habilidad": habilidad.nombre,
            "resultado": resultado
        }

    # RECIBIR DAÑO
    def Recibir_daño(self, ataque, atacante=None):

        damage = ataque - (ataque * (self.Def / 100))
        damage = max(1, int(damage))

        self.HP -= damage

        # animación
        self.anim_state = "hurt"
        self.anim_timer = 15
        self.shake = 8

        if self.HP <= 0:
            self.HP = 0
            return "dead"

        return damage

    # CURACIÓN
    def Heal(self, heal):

        heal = int(heal)
        self.HP = min(self.Base_HP, self.HP + heal)

        self.anim_state = "heal"
        self.anim_timer = 15

        return heal
    
    #  RESTAURAR STATS
    def restore_stats(self):

        self.HP = self.Base_HP
        self.MP = self.Base_MP
        self.Atk = self.Base_Atk
        self.Def = self.Base_Def
        self.Spd = self.Base_Spd

        # limpiar estados
        self.Debuff = "Normal"
        self.duration_debuff = 0

        self.Buff = "Normal"
        self.duration_buff = 0

    # 



    # USAR POCIÓN
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

        self.anim_state = "heal"
        self.anim_timer = 10

        return curacion_real

    #  VALOR DE VENTA
    def obtener_valor_venta(self):

        rango = self.Characteristics.rank  # 🔧 corregido

        valores = {
            "S": 200,
            "A": 100,
            "B": 60,
            "C": 30,
            "D": 15
        }

        return valores.get(rango, 10)

    #  SAVE
    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "Class": self.Class,
            "Type": self.Type,
            "HP": self.Base_HP,
            "MP": self.Base_MP,
            "Atk": self.Base_Atk,
            "Def": self.Base_Def,
            "Spd": self.Base_Spd,
            "skills": [s.nombre for s in getattr(self, "habilidades", [])]
        }
       