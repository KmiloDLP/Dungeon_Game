from ..Skill_Base import *
from ..Skills_function import *


SKILLS_AIR = [

    # daño
    Habilidad("Corte de Viento","Air", Damage_skills, bonus=1.3),
    Habilidad("Torbellino","Air", Damage_skills, bonus=1.4),
    Habilidad("Onda","Air", Damage_skills, bonus=1.2),
    Habilidad("Huracán","Air", Damage_skills, bonus=1.7),
    Habilidad("Viento Cortante","Air", Damage_skills, bonus=1.5),

    # utilidad (velocidad, evasión, presión)
    Habilidad("Velocidad Extrema","Air", Buff_Stats, stat="Spd", bonus=0.5),
    Habilidad("Evasión","Air",Status_modification,state="Dodge",duration=2, debuff=False),
    Habilidad("Golpes Rápidos","Air",multi_hit,bonus=0.5,max_hits=4,variability=0.8),
    Habilidad("Desorientar","Air", Debuff_Stats, stat="Atk", bonus=0.3),
    Habilidad("Corriente","Air",Buff_debuff,stat1="Spd", bonus1=0.4,stat2="Def", bonus2=0.2),
]
