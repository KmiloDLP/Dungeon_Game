import random
from cartas import Drains
from cartas import Dragons
from cartas import Golems
from cartas import Cristalize
from cartas import Spirits
from cartas import Immortals
from cartas import Wizards
from cartas import Warriors
from cartas import Regenerators


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
            "Cristalize": ["Tierra", "Aire", "Planta", "Luz"],
            "Dragon": ["Tierra", "Agua", "Fuego", "Aire", "Oscuridad"],
            "Drain": ["Agua", "Aire", "Planta", "Metal", "Oscuridad"],
            "Golem": ["Tierra", "Fuego", "Planta", "Metal"],
            "Immortal": ["Agua", "Fuego", "Metal", "Luz"],
            "Regenerator": ["Tierra", "Agua", "Planta", "Metal", "Luz"],
            "Spirit": ["Agua", "Fuego", "Aire", "Oscuridad", "Luz"],
            "Warrior": ["Tierra", "Aire", "Metal", "Oscuridad", "Luz"],
            "Wizard": ["Agua", "Fuego", "Planta", "Oscuridad"],
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
        spd = generar_stat(10, 50)
        mp  = generar_stat(100, 200)

  
        Classes = {
            "Golem": Golems.Golems,
            "Dragon": Dragons.Dragons,
            "Drain": Drains.Drains,
            "Spirit": Spirits.Spirits,
            "Warrior": Warriors.Warriors,
            "Wizard": Wizards.Wizards,
            "Regenerator": Regenerators.Regenerators,
            "Immortal": Immortals.Immortals,
            "Cristalize": Cristalize.Cristalize
        }

        clase_obj = Classes[clase]
        carta = clase_obj(tipo, hp, mp, atk, deff, spd)


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
