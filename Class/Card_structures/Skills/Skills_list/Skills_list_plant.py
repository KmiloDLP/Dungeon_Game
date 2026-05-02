from ..Skill_Base import *
from ..Skills_function import *


SKILLS_PLANT = [

    # daño
    Habilidad("Enredadera","Plant", Damage_skills, bonus=1.2),
    Habilidad("Espinas","Plant", Damage_skills, bonus=1.3),
    Habilidad("Raíz Golpe","Plant", Damage_skills, bonus=1.1),
    Habilidad("Flor Explosiva","Plant", Damage_skills, bonus=1.5),
    Habilidad("Latigazo Verde","Plant", Damage_skills, bonus=1.4),

    # utilidad (sustain y control)
    Habilidad("Fotosíntesis","Plant", Healings, bonus=0.4),
    Habilidad("Esporas","Plant",Status_modification,state="Poison",duration=3),
    Habilidad("Enredo","Plant", Debuff_Stats, stat="Spd", bonus=0.4),
    Habilidad("Crecimiento","Plant", Buff_Stats, stat="Def", bonus=0.3),
    Habilidad("Absorber Vida","Plant",Drain_hp,bonus_damage=1.1,bonus_heal=0.3),
]