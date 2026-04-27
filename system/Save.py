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

    ORDEN_POCIONES = {
    "Minipocion": 1,
    "Pocion": 2,
    "Superpocion": 3,
    "Hiperpocion": 4,
}
    try:
        with open("save.json", "r") as f:
            data = json.load(f)

        game.mazo = [crear_carta_desde_dict(c) for c in data["mazo"]]
        inventario = data.get("inventario", {})
        game.oro = data["oro"]

        game.inventario = dict(
            sorted(
                inventario.items(),
                key=lambda item: ORDEN_POCIONES.get(item[0], 999)
            )
        )

    except FileNotFoundError:
        print("No hay partida guardada")