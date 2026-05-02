from .Skills_list.Skills_list_dark import SKILLS_DARK
from .Skills_list.Skills_list_earth import SKILLS_EARTH
from .Skills_list.Skills_list_fire import SKILLS_FIRE
from .Skills_list.Skills_list_light import SKILLS_LIGHT
from .Skills_list.Skills_list_metal import SKILLS_METAL
from .Skills_list.Skills_list_physical import SKILLS_PHYSICAL
from .Skills_list.Skills_list_plant import SKILLS_PLANT
from .Skills_list.Skills_list_water import SKILLS_WATER
from .Skills_list.Skills_list_air import SKILLS_AIR


SKILLS_BY_TYPE  = {
    "Fire": SKILLS_FIRE,
    "Water": SKILLS_WATER,
    "Earth": SKILLS_EARTH,
    "Air": SKILLS_AIR,
    "Light": SKILLS_LIGHT,
    "Dark": SKILLS_DARK,
    "Plant": SKILLS_PLANT,
    "Metal": SKILLS_METAL,
}

ALL_SKILL_LIST = []

for skill_list in SKILLS_BY_TYPE .values():
    ALL_SKILL_LIST.extend(skill_list)

ALL_SKILL_LIST.extend(SKILLS_PHYSICAL)

SKILL_NAME_MAP = {}

for skill in ALL_SKILL_LIST:
    if not hasattr(skill, "nombre"):
        raise TypeError(f"Skill inválida detectada: {skill}")

    if skill.nombre in SKILL_NAME_MAP:
        raise ValueError(f"Nombre de habilidad duplicado: {skill.nombre}")

    SKILL_NAME_MAP[skill.nombre] = skill