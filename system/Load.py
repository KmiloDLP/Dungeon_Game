from cartas.Golems import Golems
from cartas.Lichs import Lichs

def crear_carta_desde_dict(data):
    clases = {
        "Golems": Golems,
        "Lichs": Lichs,
    }

    clase = clases.get(data["tipo"])

    if clase:
        carta = clase(data["vida_max"], data["atk"])
        carta.vida = data["vida"]
        return carta

    return None