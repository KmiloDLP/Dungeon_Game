from ..Skill_Base import *
from ..Skills_function import *


SKILLS_FIRE = [

    # daño
    Habilidad("Llamarada", Damage_skills, bonus=1.3),
    Habilidad("Explosión Ígnea", Damage_skills, bonus=1.6),
    Habilidad("Fuego Salvaje", Damage_skills, bonus=1.2),
    Habilidad("Infierno", Damage_skills, bonus=1.8),
    Habilidad("Chispa", Damage_skills, bonus=1.1),

    # utilidad (ofensivo + riesgo/recompensa)
    Habilidad("Ira Ardiente", Buff_Stats, stat="Atk", bonus=0.3),
    Habilidad("Sobrecalentar",Buff_debuff,stat1="Atk", bonus1=0.4,stat2="Def", bonus2=0.2),
    Habilidad("Combustión",Status_modification,state="Burn",duration=3),
    Habilidad("Ráfaga Ígnea",multi_hit,bonus=0.6,max_hits=3,variability=0.7),
    Habilidad("Sacrificio Ígneo",Drain_hp,bonus_damage=1.4,bonus_heal=0.2)
]
