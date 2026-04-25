import json
from system.Load import crear_carta_desde_dict

def guardar_juego(game):
    data = {
        "mazo": [c.to_dict() for c in game.mazo],
        "inventario": game.inventario,
        "oro": game.oro
    }

    with open("save.json", "w") as f:
        json.dump(data, f, indent=4)


def cargar_juego(game):
    try:
        with open("save.json", "r") as f:
            data = json.load(f)

        game.mazo = [crear_carta_desde_dict(c) for c in data["mazo"]]
        game.inventario = data["inventario"]
        game.oro = data["oro"]

    except FileNotFoundError:
        print("No hay partida guardada")