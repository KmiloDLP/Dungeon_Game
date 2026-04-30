from cartas.Cristalize import Cristalize
from cartas.Dragons import Dragons
from cartas.Spirits import Spirits
from cartas.Immortals import Immortals
from cartas.Golems import Golems
from cartas.Wizards import Wizards
from cartas.Warriors import Warriors
from cartas.Regenerators import Regenerators
from cartas.Drains import Drains


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

    carta = clase(
        data["Type"],
        data["HP"],   # ← antes Base_HP
        data["MP"],
        data["Atk"],
        data["Def"],
        data["Spd"]
    )

    return carta