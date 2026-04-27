import pygame
from Ui.draw_cart import draw_item, draw_text

class InventarioState:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 40)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 30))

        width = screen.get_width()

        font_path = "./Ui/fonts/DeutscheZierschrift.ttf"
        self.font = pygame.font.Font(font_path, 40)

        titulo = "Inventario"

        draw_text(
                screen,
                titulo,
                self.font,
                col=(255,255,255),
                center=True,
                pos=(width//2, 50)
            )


        start_x = width // 2 - (4 * 200 + (4 - 1) * 40) // 2
        start_y = 100

        items = [("Oro", self.game.oro)] + list(self.game.inventario.items())

        for i, (item, cantidad) in enumerate(items):

            col = i % 4
            fila = i // 4

            x = start_x + col * (200 + 40)
            y = start_y + fila * (300 + 40) 

            draw_item(screen, item, x, y, cantidad)