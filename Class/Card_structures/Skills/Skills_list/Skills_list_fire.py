from ..Skill_Base import *
from ..Skills_function import *


SKILLS_FIRE = [

    # daño
    Habilidad("Llamarada","Fire", Damage_skills, bonus=1.3),
    Habilidad("Explosión Ígnea","Fire", Damage_skills, bonus=1.6),
    Habilidad("Fuego Salvaje","Fire", Damage_skills, bonus=1.2),
    Habilidad("Infierno","Fire", Damage_skills, bonus=1.8),
    Habilidad("Chispa","Fire", Damage_skills, bonus=1.1),

    # utilidad (ofensivo + riesgo/recompensa)
    Habilidad("Ira Ardiente","Fire", Buff_Stats, stat="Atk", bonus=0.3),
    Habilidad("Sobrecalentar","Fire",Buff_debuff,stat1="Atk", bonus1=0.4,stat2="Def", bonus2=0.2),
    Habilidad("Combustión","Fire",Status_modification,state="Burn",duration=3),
    Habilidad("Ráfaga Ígnea","Fire",multi_hit,bonus=0.6,max_hits=3,variability=0.7),
    Habilidad("Sacrificio Ígneo","Fire",Drain_hp,bonus_damage=1.4,bonus_heal=0.2)
]
