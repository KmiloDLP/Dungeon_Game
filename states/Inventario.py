import pygame

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

        titulo = self.font.render("Inventario", True, (255,255,255))
        screen.blit(titulo, (20, 20))

        for i, item in enumerate(self.game.inventario):
            texto = self.font.render(f"- {item}", True, (255,255,255))
            screen.blit(texto, (50, 100 + i * 40))

        # 💰 oro
        oro_text = self.font.render(f"Oro: {self.game.oro}", True, (255,215,0))
        screen.blit(oro_text, (50, 400))