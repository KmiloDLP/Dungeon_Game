from Class.Card_structures.Class.Cristalize import Cristalize
from Class.Card_structures.Class.Dragons import Dragons
from Class.Card_structures.Class.Spirits import Spirits
from Class.Card_structures.Class.Immortals import Immortals
from Class.Card_structures.Class.Golems import Golems
from Class.Card_structures.Class.Wizards import Wizards
from Class.Card_structures.Class.Warriors import Warriors
from Class.Card_structures.Class.Regenerators import Regenerators
from Class.Card_structures.Class.Drains import Drains

from Class.Card_structures.Skills.Skills_registry import SKILL_NAME_MAP


def crear_carta_desde_dict(data):

    clases = {
        "Cristalize": Cristalize,
        "Dragon": Dragons,
        "Spirit": Spirits,
        "Immortal": Immortals,
        "Golem": Golems,
        "Wizard": Wizards,
        "Warrior": Warriors,
        "Regenerator": Regenerators,
        "Drain": Drains,
    }

    clase = clases.get(data["Class"])

    if not clase:
        print(f"[WARN] Clase desconocida: {data.get('Class')}")
        return None

    # 🔥 Crear SIN habilidades automáticas
    carta = clase(
        data["Type"],
        data["HP"],
        data["MP"],
        data["Atk"],
        data["Def"],
        data["Spd"],
        auto_skills=False  # 🔥 CLAVE
    )

    # 🔥 restaurar habilidades guardadas
    if "skills" in data:
        carta.habilidades = [
            SKILL_NAME_MAP[nombre]
            for nombre in data["skills"]
            if nombre in SKILL_NAME_MAP
        ]

    return carta