from ..Skill_Base import *
from ..Skills_function import *


SKILLS_METAL = [

    # daño
    Habilidad("Corte Metálico","Metal", Damage_skills, bonus=1.3),
    Habilidad("Espada Pesada","Metal", Damage_skills, bonus=1.5),
    Habilidad("Impacto de Acero","Metal", Damage_skills, bonus=1.6),
    Habilidad("Cuchilla","Metal", Damage_skills, bonus=1.2),
    Habilidad("Perforación","Metal", Damage_skills, bonus=1.4),

    # utilidad
    Habilidad("Robo de Fuerza","Metal",steal_stats,stat="Atk",bonus=0.3),
    Habilidad("Reflejo","Metal",Status_modification,state="Reflect",duration=2, debuff=False),
    Habilidad("Precisión","Metal", Buff_Stats, stat="Atk", bonus=0.2),
    Habilidad("Armadura Viva","Metal", Buff_Stats, stat="Def", bonus=0.4),
    Habilidad("Golpe Doble","Metal",multi_hit,bonus=0.6,max_hits=2,variability=1),
]
