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

    def draw(self, screen):  # ✅ BIEN (dentro de la clase)
        screen.fill((30, 30, 30))

        titulo = self.font.render("Inventario", True, (255,255,255))
        screen.blit(titulo, (20, 20))

        y = 100
        for item, cantidad in self.game.inventario.items():
            texto = self.font.render(f"{item} x{cantidad}", True, (255,255,255))
            screen.blit(texto, (50, y))
            y += 40

        oro_text = self.font.render(f"Oro: {self.game.oro}", True, (255,215,0))
        screen.blit(oro_text, (50, 400))