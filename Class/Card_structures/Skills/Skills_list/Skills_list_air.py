from ..Skill_Base import *
from ..Skills_function import *


SKILLS_AIR = [

    # daño
    Habilidad("Corte de Viento", Damage_skills, bonus=1.3),
    Habilidad("Torbellino", Damage_skills, bonus=1.4),
    Habilidad("Onda", Damage_skills, bonus=1.2),
    Habilidad("Huracán", Damage_skills, bonus=1.7),
    Habilidad("Viento Cortante", Damage_skills, bonus=1.5),

    # utilidad (velocidad, evasión, presión)
    Habilidad("Velocidad Extrema", Buff_Stats, stat="Spd", bonus=0.5),
    Habilidad("Evasión",Status_modification,state="Dodge",duration=2),
    Habilidad("Golpes Rápidos",multi_hit,bonus=0.5,max_hits=4,variability=0.8),
    Habilidad("Desorientar", Debuff_Stats, stat="Atk", bonus=0.3),
    Habilidad("Corriente",Buff_debuff,stat1="Spd", bonus1=0.4,stat2="Def", bonus2=0.2),
]
