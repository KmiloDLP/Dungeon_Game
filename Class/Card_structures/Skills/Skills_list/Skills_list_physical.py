from ..Skill_Base import *
from ..Skills_function import *


SKILLS_PHYSICAL = [

    # daño
    Habilidad("Golpe Básico","Physical", Damage_skills, bonus=1.0),
    Habilidad("Golpe Fuerte","Physical", Damage_skills, bonus=1.4),
    Habilidad("Impacto Pesado","Physical", Damage_skills, bonus=1.8),
    Habilidad("Ataque Preciso","Physical", Damage_skills, bonus=1.2),
    Habilidad("Golpe Brutal","Physical", Damage_skills, bonus=2.0),
    Habilidad("Doble Golpe","Physical", multi_hit, bonus=0.8, max_hits=2, variability=1),
    Habilidad("Desenfreno","Physical", multi_hit, bonus=0.6, max_hits=3, variability=0.7),
    Habilidad("Combo Salvaje","Physical", multi_hit, bonus=0.5, max_hits=5, variability=0.5),
    Habilidad("Tormenta de Golpes","Physical", multi_hit, bonus=0.4, max_hits=6, variability=0.4),
    Habilidad("Cadena Rápida","Physical", multi_hit, bonus=0.7, max_hits=4, variability=0.6),

    
]


