import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

game = Game(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game.handle_event(event)

    game.update()
    game.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()