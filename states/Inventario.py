import pygame
from Ui.draw_cart import draw_item, draw_text, font_ui

class InventarioState:
    def __init__(self, game):
        self.game = game

        self.selected = 0
        self.show_info = False

        self.columnas = 4

        # 🎬 animación
        self.anim_scale = 1

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                self.selected += 1

            elif event.key == pygame.K_LEFT:
                self.selected -= 1

            elif event.key == pygame.K_DOWN:
                self.selected += self.columnas

            elif event.key == pygame.K_UP:
                self.selected -= self.columnas

            elif event.key == pygame.K_RETURN:
                self.show_info = not self.show_info
                self.anim_scale = 0.8

            elif event.key == pygame.K_ESCAPE:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

        total = len(self.get_items())
        self.selected = max(0, min(self.selected, total - 1))

    def get_items(self):
        return [("Oro", self.game.oro)] + list(self.game.inventario.items())

    def update(self):
        self.anim_scale += (1 - self.anim_scale) * 0.15

    def draw(self, screen):
        screen.fill((30, 30, 30))
        width = screen.get_width()

        draw_text(screen, "Inventario", font_ui, center=True, pos=(width//2, 50))
        draw_text(screen, "[ENTER] Ver info    [ESC] Salir", font_ui, center=True, pos=(width//2, 750))

        items = self.get_items()

        start_x = width // 2 - (4 * 200 + 3 * 40) // 2
        start_y = 100

        for i, (item, cantidad) in enumerate(items):

            col = i % 4
            fila = i // 4

            x = start_x + col * (200 + 40)
            y = start_y + fila * (300 + 40)

            seleccionado = (i == self.selected)

            scale = self.anim_scale if seleccionado else 1

            draw_item(
                screen,
                item,
                x,
                y,
                cantidad,
                info=(seleccionado and self.show_info),
                scale=scale
            )