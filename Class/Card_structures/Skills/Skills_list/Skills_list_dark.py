from ..Skill_Base import *
from ..Skills_function import *


SKILLS_DARK = [

    # daño
    Habilidad("Golpe Sombrío","Dark", Damage_skills, bonus=1.3),
    Habilidad("Oscuridad Pura","Dark", Damage_skills, bonus=1.6),
    Habilidad("Ataque Maldito","Dark", Damage_skills, bonus=1.5),
    Habilidad("Sombra Letal","Dark", Damage_skills, bonus=1.7),
    Habilidad("Impacto Vacío","Dark", Damage_skills, bonus=1.4),

    # utilidad 
    Habilidad("Maldición","Dark", Debuff_Stats, stat="Atk", bonus=0.4),
    Habilidad("Drenaje Oscuro","Dark",Drain_hp,bonus_damage=1.2,bonus_heal=0.5),
    Habilidad("Debilitamiento","Dark", Debuff_Stats, stat="Def", bonus=0.4),
    Habilidad("Sombra Viva","Dark",Status_modification,state="Blind",duration=2),
    Habilidad("Robo Total","Dark",steal_stats,stat="Atk",bonus=0.4),
]
