import pygame

class MenuState:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 50)

        self.options = ["Luchar", "Mazo", "Inventario", "Salir"]
        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                self.select_option()

    def select_option(self):
        opcion = self.options[self.selected]

        if opcion == "Luchar":
            from states.combate import CombatState
            self.game.change_state(CombatState(self.game))
        elif opcion == "Salir":
            pygame.quit()
            exit()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))

        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i != self.selected else (255, 0, 0)
            text = self.font.render(option, True, color)
            screen.blit(text, (350, 200 + i * 60))