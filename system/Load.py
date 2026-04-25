from cartas.Cristalize import Cristalize
from cartas.Dragones import Dragones
from cartas.Fantasmas import Fantasmas
from cartas.Fenixs import Fenixs
from cartas.Golems import Golems
from cartas.Lichs import Lichs
from cartas.Ogros import Ogros
from cartas.Troll import Trolls
from cartas.Vampiro import Vampiros




def crear_carta_desde_dict(data):
    clases = {
        "Golems": Golems,
        "Lichs": Lichs,
        "Fantasmas": Fantasmas,
        "Fenixs": Fenixs,
        "Ogros": Ogros,
        "Trolls": Trolls,
        "Vampiros": Vampiros,
        "Cristalize": Cristalize,
        "Dragones": Dragones,    
    }

    clase = clases.get(data["tipo"])

    if clase:

        if clase == Lichs:
                carta = clase(data["vida_max"]*2, data["atk"]/2)
        else:
            carta = clase(data["vida_max"], data["atk"])
            carta.vida = data["vida"]
        return carta

    return None