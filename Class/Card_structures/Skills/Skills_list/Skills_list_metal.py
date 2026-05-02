from ..Skill_Base import *
from ..Skills_function import *


SKILLS_METAL = [

    # daño
    Habilidad("Corte Metálico", Damage_skills, bonus=1.3),
    Habilidad("Espada Pesada", Damage_skills, bonus=1.5),
    Habilidad("Impacto de Acero", Damage_skills, bonus=1.6),
    Habilidad("Cuchilla", Damage_skills, bonus=1.2),
    Habilidad("Perforación", Damage_skills, bonus=1.4),

    # utilidad
    Habilidad("Robo de Fuerza",steal_stats,stat="Atk",bonus=0.3),
    Habilidad("Reflejo",Status_modification,state="Reflect",duration=2),
    Habilidad("Precisión", Buff_Stats, stat="Atk", bonus=0.2),
    Habilidad("Armadura Viva", Buff_Stats, stat="Def", bonus=0.4),
    Habilidad("Golpe Doble",multi_hit,bonus=0.6,max_hits=2,variability=1),
]
