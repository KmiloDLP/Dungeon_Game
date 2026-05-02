from ..Skill_Base import *
from ..Skills_function import *


SKILLS_WATER = [

    # daño
    Habilidad("Torrente", Damage_skills, bonus=1.3),
    Habilidad("Marea", Damage_skills, bonus=1.2),
    Habilidad("Presión Marina", Damage_skills, bonus=1.5),
    Habilidad("Ola Gigante", Damage_skills, bonus=1.7),
    Habilidad("Salpicadura", Damage_skills, bonus=1.0),

    # utilidad (flujo, sustain)
    Habilidad("Regeneración", Healings, bonus=0.3),
    Habilidad("Absorción",Drain_hp,bonus_damage=1.0,bonus_heal=0.4),
    Habilidad("Corriente Lenta", Debuff_Stats, stat="Spd", bonus=0.3),
    Habilidad("Flujo Vital", Buff_Stats, stat="HP", bonus=0.2),
    Habilidad("Purificación",Status_modification,state="Cleanse",duration=1),
]

