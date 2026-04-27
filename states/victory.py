import pygame
from Ui.draw_cart import draw_text, draw_card, draw_item
from system.Save import guardar_juego


class VictoryState:

    def __init__(self, game, player, enemy, recompensa):
        self.game = game
        self.player = player
        self.enemy = enemy
        self.recompensa = recompensa

        self.font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 30)

        self.apply_reward()


    def apply_reward(self):

        if isinstance(self.recompensa, int):
            self.game.oro += self.recompensa

        elif isinstance(self.recompensa, str):
            if self.recompensa in self.game.inventario:
                self.game.inventario[self.recompensa] += 1
            else:
                self.game.inventario[self.recompensa] = 1

        else:
            self.game.mazo.append(self.recompensa)

        guardar_juego(self.game)


    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

            elif event.key == pygame.K_ESCAPE:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

    def update(self):
        pass


    def draw(self, screen):

        screen.fill((20, 20, 20))
        width = screen.get_width()

        font_path = "./Ui/fonts/DeutscheZierschrift.ttf"
        self.font = pygame.font.Font(font_path, 40)

        # 🏆 título

        draw_text(screen," VICTORIA", self.font, col=(255,255,255), center=True, pos=(width//2, 80))

        # enemigo derrotado
        draw_text(screen, f"Derrotaste a {self.enemy.nombre}",
                  self.small_font, center=True, pos=(width//2, 150))

        draw_text(screen," Recompensa", self.font, col=(255,255,255), center=True, pos=(width//2, 250))


        # mostrar recompensa
        if isinstance(self.recompensa, int):
            draw_item(screen, "Oro", (width//2)-100, 300, self.recompensa)

        elif isinstance(self.recompensa, str):
            draw_item(screen, self.recompensa, (width//2)-100, 300, 1)

        else:
            draw_card(screen, self.recompensa, width//2 - 100, 300)

        # hint
        draw_text(screen, "ENTER continuar",self.font, center=True, pos=(width//2, 700)) 