import pygame
from Ui.draw_cart import draw_card, draw_text, font_ui


class MazoState:
    def __init__(self, game):
        self.game = game

        self.scroll = 0
        self.columnas = 3
        self.filas_visibles = 2

        self.CARD_W, self.CARD_H = 200, 300
        self.ESP_Y = 20
        self.START_Y = 120

        self.selected = 0
        self.show_info = False

        # 🎬 animación
        self.anim_scale = 1
        self.anim_target = 1

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                self.selected = min(self.selected + 1, len(self.game.mazo) - 1)

            elif event.key == pygame.K_LEFT:
                self.selected = max(self.selected - 1, 0)

            elif event.key == pygame.K_DOWN:
                self.selected = min(self.selected + self.columnas, len(self.game.mazo) - 1)

            elif event.key == pygame.K_UP:
                self.selected = max(self.selected - self.columnas, 0)

            elif event.key == pygame.K_RETURN:
                self.show_info = not self.show_info
                self.anim_scale = 0.8  # 👈 efecto flip

            elif event.key == pygame.K_ESCAPE:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

    def update(self):
        # 🎬 animación suave
        self.anim_scale += (1 - self.anim_scale) * 0.15

    def draw(self, screen):
        screen.fill((20, 20, 20))
        width = screen.get_width()

        draw_text(screen, "Mazo", font_ui, center=True, pos=(width//2, 50))
        draw_text(screen, "[ENTER] Ver info    [ESC] Salir", font_ui, center=True, pos=(width//2, 750))

        cartas = self.game.mazo

        columnas_x = [width * 0.25, width * 0.5, width * 0.75]

        for i, carta in enumerate(cartas):
            col = i % self.columnas
            fila = i // self.columnas

            x = columnas_x[col] - self.CARD_W // 2
            y = self.START_Y + fila * (self.CARD_H + self.ESP_Y)

            seleccionado = (i == self.selected)

            # 🎬 animación solo en la seleccionada
            scale = self.anim_scale if seleccionado else 1

            draw_card(
                screen,
                carta,
                x,
                y,
                info=(seleccionado and self.show_info),
                scale=scale
            )