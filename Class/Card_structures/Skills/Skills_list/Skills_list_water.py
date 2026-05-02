from ..Skill_Base import *
from ..Skills_function import *


SKILLS_WATER = [

    # daño
    Habilidad("Torrente","Water", Damage_skills, bonus=1.3),
    Habilidad("Marea","Water", Damage_skills, bonus=1.2),
    Habilidad("Presión Marina","Water", Damage_skills, bonus=1.5),
    Habilidad("Ola Gigante","Water", Damage_skills, bonus=1.7),
    Habilidad("Salpicadura","Water", Damage_skills, bonus=1.0),

    # utilidad (flujo, sustain)
    Habilidad("Regeneración", "Water",Healings, bonus=0.3),
    Habilidad("Absorción","Water",Drain_hp,bonus_damage=1.0,bonus_heal=0.4),
    Habilidad("Corriente Lenta","Water", Debuff_Stats, stat="Spd", bonus=0.3),
    Habilidad("Flujo Vital","Water", Buff_Stats, stat="HP", bonus=0.2),
    Habilidad("Purificación","Water",Status_modification,state="Cleanse",duration=1),
]

