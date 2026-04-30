import os

class Marco:
    def __init__(self, Class, Type, HP, Def, Atk, Spd, Mp):

        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "img")


        self.rank = self.calcular_rank_general(HP, Def, Atk, Spd, Mp)
        self.nombre = self.Assign_name(Class, Type)

        self.sprite = os.path.join(img_dir, "cartas", f"{Class.lower()}_{Type.lower()}.png")
        print(f"{Class.lower()}_{Type.lower()}.png")
        self.fondo = os.path.join(img_dir, "fondos", f"{self.rank}.png")
        self.class_icon = os.path.join(img_dir, "Class", f"{Class}.png")
        self.type_icon = os.path.join(img_dir, "Types", f"{Type}.png")

    @staticmethod
    def calcular_rank_general(HP, Def, Atk, Spd, Mp):

        def rank_stat(valor, minimo, maximo):
            rango = maximo - minimo

            t1 = minimo + rango * 0.4
            t2 = minimo + rango * 0.7
            t3 = minimo + rango * 0.9

            if valor <= t1:
                return "D"
            elif valor <= t2:
                return "C"
            elif valor <= t3:
                return "B"
            else:
                return "A"

        # evaluar cada stat
        ranks = [
            rank_stat(Atk, 10, 50),
            rank_stat(HP, 50, 200),
            rank_stat(Def, 1, 30),
            rank_stat(Spd, 10, 100),
            rank_stat(Mp, 100, 200)
        ]

        valores = {"A": 4, "B": 3, "C": 2, "D": 1}

        total = sum(valores[r] for r in ranks)

        # promedio ponderado
        promedio = total / len(ranks)

        # rank final
        if promedio >= 3.5:
            return "S"
        elif promedio >= 3.0:
            return "A"
        elif promedio >= 2.5:
            return "B"
        elif promedio >= 2.0:
            return "C"
        else:
            return "D"

    @staticmethod
    def Assign_name(Class, Type):
        Names = {
            ("Cristalize","Tierra"): "Geocristal",
            ("Cristalize","Aire"): "Aerocristal",
            ("Cristalize","Planta"): "Biocristal",
            ("Cristalize","Luz"): "Fotocristal",

            ("Dragon","Tierra"): "Behemon",
            ("Dragon","Agua"): "Leviathan",
            ("Dragon","Fuego"): "Fafnir",
            ("Dragon","Aire"): "Dvalin",
            ("Dragon","Oscuridad"): "Necron",

            ("Drain","Agua"): "Lamprea",
            ("Drain","Aire"): "Kauryj",
            ("Drain","Planta"): "Driada",
            ("Drain","Metal"): "Lamia",
            ("Drain","Oscuridad"): "Vampiro",

            ("Golem","Tierra"): "Coloso",
            ("Golem","Fuego"): "Magmático",
            ("Golem","Planta"): "Treant",
            ("Golem","Metal"): "Titán",

            ("Immortal","Agua"): "Turritopsis",
            ("Immortal","Fuego"): "Fénix",
            ("Immortal","Metal"): "Centinela",
            ("Immortal","Luz"): "Ángel",

            ("Regenerator","Tierra"): "Gárgola",
            ("Regenerator","Agua"): "Hydra",
            ("Regenerator","Planta"): "Slime",
            ("Regenerator","Metal"): "Troll",
            ("Regenerator","Luz"): "Santa",

            ("Spirit","Agua"): "Undine",
            ("Spirit","Fuego"): "Ifrit",
            ("Spirit","Aire"): "Sylph",
            ("Spirit","Oscuridad"): "Banshee",
            ("Spirit","Luz"): "Soul",

            ("Warrior","Tierra"): "Minotauro",
            ("Warrior","Aire"): "Falcón",
            ("Warrior","Metal"): "Ogro",
            ("Warrior","Oscuridad"): "Ghoul",
            ("Warrior","Luz"): "Paladín",

            ("Wizard","Agua"): "Mermaid",
            ("Wizard","Fuego"): "Piromante",
            ("Wizard","Planta"): "Druida",
            ("Wizard","Oscuridad"): "Lich",
        }

        return Names.get((Class, Type), f"{Class} {Type}")