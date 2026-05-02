from ..Skill_Base import *
from ..Skills_function import *


SKILLS_LIGHT = [

    # daño
    Habilidad("Rayo de Luz", Damage_skills, bonus=1.3),
    Habilidad("Explosión Sagrada", Damage_skills, bonus=1.6),
    Habilidad("Golpe Divino", Damage_skills, bonus=1.5),
    Habilidad("Purga", Damage_skills, bonus=1.4),
    Habilidad("Juicio", Damage_skills, bonus=1.7),

    # utilidad
    Habilidad("Bendición", Buff_Stats, stat="Atk", bonus=0.3),
    Habilidad("Protección", Buff_Stats, stat="Def", bonus=0.4),
    Habilidad("Sanar", Healings, bonus=0.4),
    Habilidad("Bautizo", Status_modification, state="Cleanse", duration=1),
    Habilidad("Aura Sagrada",Buff_debuff,stat1="Def", bonus1=0.3,stat2="Atk", bonus2=0.1),

]