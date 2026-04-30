import json
from system.Load import crear_carta_desde_dict

ORDEN_POCIONES = {
    "Minipocion": 1,
    "Pocion": 2,
    "Superpocion": 3,
    "Hiperpocion": 4,
}

def guardar_juego(game):
    data = {
        "mazo": [c.to_dict() for c in game.mazo],
        "inventario": game.inventario,
        "oro": game.oro
    }

    with open("save.json", "w") as f:
        json.dump(data, f, indent=4)
        f.flush()


def cargar_juego(game):
    try:
        with open("save.json", "r") as f:
            contenido = f.read().strip()

            if not contenido:
                raise ValueError("Archivo vacío")

            data = json.loads(contenido)

        game.mazo = [
            crear_carta_desde_dict(c) 
            for c in data.get("mazo", [])
            if c is not None
        ]

        inventario = data.get("inventario", {})
        game.oro = data.get("oro", 0)

        game.inventario = dict(
            sorted(
                inventario.items(),
                key=lambda item: ORDEN_POCIONES.get(item[0], 999)
            )
        )

    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        print("⚠️ Save inválido → creando nuevo")

        game.mazo = []
        game.inventario = {}
        game.oro = 0