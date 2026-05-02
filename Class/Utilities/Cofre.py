import random
from Class.Card_structures.Class.Drains import Drains
from Class.Card_structures.Class.Dragons import Dragons
from Class.Card_structures.Class.Golems import Golems
from Class.Card_structures.Class.Cristalize import Cristalize
from Class.Card_structures.Class.Spirits import Spirits
from Class.Card_structures.Class.Immortals import Immortals
from Class.Card_structures.Class.Wizards import Wizards
from Class.Card_structures.Class.Warriors import Warriors
from Class.Card_structures.Class.Regenerators import Regenerators


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

        Types = {
            "Cristalize": ["Earth", "Air", "Plant", "Light"],
            "Dragon": ["Earth", "Water", "Fire", "Air", "Dark"],
            "Drain": ["Water", "Air", "Plant", "Metal", "Dark"],
            "Golem": ["Earth", "Fire", "Plant", "Metal"],
            "Immortal": ["Water", "Fire", "Metal", "Light"],
            "Regenerator": ["Earth", "Water", "Plant", "Metal", "Light"],
            "Spirit": ["Water", "Fire", "Air", "Dark", "Light"],
            "Warrior": ["Earth", "Air", "Metal", "Dark", "Light"],
            "Wizard": ["Water", "Fire", "Plant", "Dark"],
        }

        clase = random.choice(list(Types.keys()))
        tipo = random.choice(Types[clase])

        def generar_stat(minimo, maximo):
            r = random.random()
            rango = maximo - minimo

            if r <= 0.4:
                return random.randint(minimo, int(minimo + rango * 0.4))
            elif r <= 0.7:
                return random.randint(int(minimo + rango * 0.4), int(minimo + rango * 0.7))
            elif r <= 0.9:
                return random.randint(int(minimo + rango * 0.7), int(minimo + rango * 0.9))
            else:
                return random.randint(int(minimo + rango * 0.9), maximo)

        hp  = generar_stat(50, 200)
        atk = generar_stat(10, 50)
        deff = generar_stat(1, 30)
        spd = generar_stat(10, 100)  # ✔ corregido
        mp  = generar_stat(100, 200)

        Classes = {
            "Golem": Golems,
            "Dragon": Dragons,
            "Drain": Drains,
            "Spirit": Spirits,
            "Warrior": Warriors,
            "Wizard": Wizards,
            "Regenerator": Regenerators,
            "Immortal": Immortals,
            "Cristalize": Cristalize
        }

        clase_obj = Classes[clase]

        carta = clase_obj(tipo, hp, mp, atk, deff, spd, auto_skills=True)

        return carta

    def generar_objeto(self):
        if self.rango == "A":
            return "Hiperpocion"
        elif self.rango == "B":
            return "Superpocion"
        elif self.rango == "C":
            return "Pocion"
        else:
            return "Minipocion"

    def generar_oro(self):
        if self.rango == "A":
            return random.randint(91, 120)
        elif self.rango == "B":
            return random.randint(61, 90)
        elif self.rango == "C":
            return random.randint(31, 60)
        else:
            return random.randint(10, 30)
