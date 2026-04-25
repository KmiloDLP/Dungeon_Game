import pygame
from Ui.draw_cart import draw_card

class MazoState:
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
        screen.fill((20, 20, 20))

        titulo = self.font.render("Mazo", True, (255,255,255))
        screen.blit(titulo, (20, 20))

        x, y = 50, 100
        for i, carta in enumerate(self.game.mazo):
            draw_card(screen, carta, x, y)

            x += 220
            if x > 700:
                x = 50
                y += 320