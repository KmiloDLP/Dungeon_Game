from ..Skill_Base import *
from ..Skills_function import *


SKILLS_LIGHT = [

    # daño
    Habilidad("Rayo de Luz","Light", Damage_skills, bonus=1.3),
    Habilidad("Explosión Sagrada","Light", Damage_skills, bonus=1.6),
    Habilidad("Golpe Divino","Light", Damage_skills, bonus=1.5),
    Habilidad("Purga","Light", Damage_skills, bonus=1.4),
    Habilidad("Juicio","Light", Damage_skills, bonus=1.7),

    # utilidad
    Habilidad("Bendición","Light", Buff_Stats, stat="Atk", bonus=0.3),
    Habilidad("Protección","Light", Buff_Stats, stat="Def", bonus=0.4),
    Habilidad("Sanar","Light",Healings, bonus=0.4),
    Habilidad("Bautizo","Light", Status_modification, state="Cleanse", duration=1),
    Habilidad("Aura Sagrada","Light",Buff_debuff,stat1="Def", bonus1=0.3,stat2="Atk", bonus2=0.1),

]