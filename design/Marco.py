import os

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

        # 📁 Rutas base
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "img")

        # =========================
        # 🟡 FONDO POR RANK
        # =========================
        self.ruta_fondo = os.path.join(img_dir, "fondos", f"{self.rank}.png")

        if not os.path.exists(self.ruta_fondo):
            print(f"[WARN] No existe fondo para rank {self.rank}")
            self.ruta_fondo = None

        # =========================
        # 🎴 IMAGEN DE CARTA
        # =========================
        nombre_img = f"{nombre.lower()}.png"
        self.ruta_imagen = os.path.join(img_dir, "cartas", nombre_img)

        if not os.path.exists(self.ruta_imagen):
            print(f"[WARN] No existe imagen para {nombre}")
            self.ruta_imagen = None