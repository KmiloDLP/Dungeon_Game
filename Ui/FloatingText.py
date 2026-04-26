
import pygame

class FloatingText:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color

        self.timer = 60  # duración
        self.dy = -1.5   # movimiento hacia arriba

        self.font = pygame.font.Font(None, 36)

    def update(self):
        self.y += self.dy
        self.timer -= 1

    def draw(self, screen):
        alpha = max(0, int(255 * (self.timer / 60)))

        surf = self.font.render(self.text, True, self.color).convert_alpha()
        surf.set_alpha(alpha)

        screen.blit(surf, (self.x, self.y))

    def alive(self):
        return self.timer > 0