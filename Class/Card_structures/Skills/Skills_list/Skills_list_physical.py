from ..Skill_Base import *
from ..Skills_function import *


SKILLS_PHYSICAL = [

    # daño
    Habilidad("Golpe Básico","Physical", Damage_skills, bonus=1.0),
    Habilidad("Golpe Fuerte","Physical", Damage_skills, bonus=1.4),
    Habilidad("Impacto Pesado","Physical", Damage_skills, bonus=1.8),
    Habilidad("Ataque Preciso","Physical", Damage_skills, bonus=1.2),
    Habilidad("Golpe Brutal","Physical", Damage_skills, bonus=2.0),
    Habilidad("Doble Golpe","Physical", multi_hit, bonus=0.8, limite=2, probabilidad=1),
    Habilidad("Desenfreno","Physical", multi_hit, bonus=0.6, limite=3, probabilidad=0.7),
    Habilidad("Combo Salvaje","Physical", multi_hit, bonus=0.5, limite=5, probabilidad=0.5),
    Habilidad("Tormenta de Golpes","Physical", multi_hit, bonus=0.4, limite=6, probabilidad=0.4),
    Habilidad("Cadena Rápida","Physical", multi_hit, bonus=0.7, limite=4, probabilidad=0.6),

    
]


