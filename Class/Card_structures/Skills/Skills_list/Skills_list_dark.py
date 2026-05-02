from ..Skill_Base import *
from ..Skills_function import *


SKILLS_DARK = [

    # daño
    Habilidad("Golpe Sombrío", Damage_skills, bonus=1.3),
    Habilidad("Oscuridad Pura", Damage_skills, bonus=1.6),
    Habilidad("Ataque Maldito", Damage_skills, bonus=1.5),
    Habilidad("Sombra Letal", Damage_skills, bonus=1.7),
    Habilidad("Impacto Vacío", Damage_skills, bonus=1.4),

    # utilidad 
    Habilidad("Maldición", Debuff_Stats, stat="Atk", bonus=0.4),
    Habilidad("Drenaje Oscuro",Drain_hp,bonus_damage=1.2,bonus_heal=0.5),
    Habilidad("Debilitamiento", Debuff_Stats, stat="Def", bonus=0.4),
    Habilidad("Sombra Viva",Status_modification,state="Blind",duration=2),
    Habilidad("Robo Total",steal_stats,stat="Atk",bonus=0.4),
]
