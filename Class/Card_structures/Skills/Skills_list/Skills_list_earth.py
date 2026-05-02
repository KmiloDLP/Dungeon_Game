from ..Skill_Base import *
from ..Skills_function import *


SKILLS_EARTH = [

    # daño
    Habilidad("Golpe Sísmico", Damage_skills, bonus=1.4),
    Habilidad("Roca Pesada", Damage_skills, bonus=1.5),
    Habilidad("Avalancha", Damage_skills, bonus=1.7),
    Habilidad("Impacto Terrestre", Damage_skills, bonus=1.3),
    Habilidad("Puño de Piedra", Damage_skills, bonus=1.2),

    # utilidad (defensa y resistencia)
    Habilidad("Fortaleza", Buff_Stats, stat="Def", bonus=0.5),
    Habilidad("Endurecer",Buff_debuff,stat1="Def", bonus1=0.4,stat2="Spd", bonus2=0.2),
    Habilidad("Armadura Natural",Status_modification,state="Shield",duration=3),
    Habilidad("Contraataque",multi_hit,bonus=0.7,max_hits=2,variability=1),
    Habilidad("Resistencia", Healings, bonus=0.2),
]

