import pygame
from Ui.draw_cart import draw_text


class MenuState:
    def __init__(self, game):
        self.game = game

        font_path = "./Ui/fonts/DeutscheZierschrift.ttf"
        self.font = pygame.font.Font(font_path, 40)

        self.options = ["Luchar", "Mazo", "Inventario", "Salir"]
        self.selected = 0

        # 🎬 offsets para animación suave
        self.offsets = [0] * len(self.options)

    # -------------------------
    # 🎮 INPUT
    # -------------------------
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)

            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)

            elif event.key == pygame.K_RETURN:
                self.select_option()

    # -------------------------
    # ⚙️ LÓGICA
    # -------------------------
    def select_option(self):
        opcion = self.options[self.selected]

        if opcion == "Luchar":
            from States.Selecc_Cart import SeleccionCartaState
            self.game.change_state(SeleccionCartaState(self.game))

        elif opcion == "Mazo":
            from States.Mazo import MazoState
            self.game.change_state(MazoState(self.game))

        elif opcion == "Inventario":
            from States.Inventario import InventarioState
            self.game.change_state(InventarioState(self.game))

        elif opcion == "Salir":
            pygame.quit()
            exit()

    def update(self):
        # 🎬 animación suave de selección
        for i in range(len(self.options)):
            target = -12 if i == self.selected else 0
            self.offsets[i] += (target - self.offsets[i]) * 0.2

    # -------------------------
    # 🎨 DIBUJO
    # -------------------------
    def draw(self, screen):
        screen.fill((0, 0, 0))

        width = screen.get_width()

        for i, option in enumerate(self.options):

            # posición vertical con separación
            base_y = 200 + i * 70
            y = base_y + self.offsets[i]

            # 🎨 color dinámico
            if i == self.selected:
                color = (255, 255, 0)  # amarillo
            else:
                color = (255, 255, 255)

            draw_text(
                screen,
                option,
                self.font,
                col=color,
                center=True,
                pos=(width // 2, y)
            )