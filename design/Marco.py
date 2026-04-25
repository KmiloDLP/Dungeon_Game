import os
import pygame

class Marco:
    def __init__(self, rank_hp, rank_atk, nombre):
        self.nombre = nombre

        valores = {"A": 4, "B": 3, "C": 2, "D": 1}
        total = valores[rank_hp] + valores[rank_atk]

        # Rank
        if total == 8:
            self.rank = "S"
        elif total == 7:
            self.rank = "A"
        elif total == 6:
            self.rank = "B"
        elif total in (4, 5):
            self.rank = "C"
        else:
            self.rank = "D"

        # Color
        colores = {
            "S": (255, 215, 0),    # amarillo
            "A": (128, 0, 128),    # morado
            "B": (0, 0, 255),      # azul
            "C": (0, 255, 0),      # verde
            "D": (128, 128, 128)   # gris
        }
        self.color = colores[self.rank]

        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "img")


        nombre_img = f"{nombre.lower()}.png"
        ruta = os.path.join(img_dir, nombre_img)

        try:
            self.imagen = pygame.image.load(ruta).convert_alpha()
        except:
            # si no existe, carga default
            ruta_default = os.path.join(img_dir, "default.png")
            self.imagen = pygame.image.load(ruta_default).convert_alpha()

        # Opcional: escalar imagen
        self.imagen = pygame.transform.scale(self.imagen, (180, 260))

        