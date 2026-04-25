import random
from cartas import Vampiro
from cartas import Dragones
from cartas import Golems
from cartas import Cristalize
from cartas import Fantasmas
from cartas import Fenixs
from cartas import Lichs
from cartas import Ogros
from cartas import Troll


class Cofre:
    def __init__(self, rango):
        self.rango = rango
        self.contenido = self.generar_contenido()

    def generar_contenido(self):
        tipo = random.choices(
            ["carta", "objeto", "oro"],
            weights=[50, 30, 20]
        )[0]

        if tipo == "carta":
            return self.generar_carta()
        elif tipo == "objeto":
            return self.generar_objeto()
        else:
            return self.generar_oro()

    def generar_carta(self):

        criaturas = ["Golem", "Dragon", "Vampiro", "Fantasma", "Ogro", "Lich", "Troll", "Fenix", "Cristalize"]
        
        criature = random.choice(criaturas)

        rangos = {
            "A": (200, 50),
            "B": (186, 45),
            "C": (156, 37),
            "D": (110, 25)
        }

        hp_max, atk_max = rangos[self.rango]

        atk = random.randint(10, atk_max)
        hp = random.randint(50, hp_max)

        criaturas_map = {
            "Golem": Golems.Golems,
            "Dragon": Dragones.Dragones,
            "Vampiro": Vampiro.Vampiros,
            "Fantasma": Fantasmas.Fantasmas,
            "Ogro": Ogros.Ogros,
            "Lich": Lichs.Lichs,
            "Troll": Troll.Trolls,
            "Fenix": Fenixs.Fenixs,
            "Cristalize": Cristalize.Cristalize
        }

        carta = criaturas_map[criature]
        return carta(hp, atk)


    def generar_objeto(self):
        if self.rango == "A":
            return "Minipocion"
        elif self.rango == "B":
            return "Pocion"
        elif self.rango == "C":
            return "Superpocion"
        else:
            return "Hiperpocion"

    def generar_oro(self):
        if self.rango == "A":
            return random.randint(10, 30)
        elif self.rango == "B":
            return random.randint(31, 60)
        elif self.rango == "C":
            return random.randint(61, 90)
        else:
            return random.randint(91, 120)
