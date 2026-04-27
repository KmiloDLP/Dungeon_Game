import pygame
from Ui.draw_cart import draw_card, draw_text

class SeleccionCartaState:
    def __init__(self, game, enemy=None, volver_a_combate=False):
        self.game = game
        self.enemy = enemy
        self.font = pygame.font.Font(None, 40)

        self.selected = 0
        self.scroll = 0

        self.columnas = 3
        self.filas_visibles = 2

        self.CARD_W, self.CARD_H = 200, 300
        self.ESP_X, self.ESP_Y = 20, 20
        self.START_X, self.START_Y = 100, 120

        self.volver_a_combate = volver_a_combate

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
                carta = self.game.mazo[self.selected]
                from states.combate import CombatState
                self.game.change_state(CombatState(self.game, carta, self.enemy))

            elif event.key == pygame.K_ESCAPE:
                if self.volver_a_combate:
                    from states.menu import MenuState
                    self.game.change_state(MenuState(self.game))

            self.actualizar_scroll()

    def actualizar_scroll(self):
        fila_actual = self.selected // self.columnas

        if fila_actual < self.scroll:
            self.scroll = fila_actual

        elif fila_actual >= self.scroll + self.filas_visibles:
            self.scroll = fila_actual - self.filas_visibles + 1

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((20, 20, 20))

        width = screen.get_width()
        font_path = "./Ui/fonts/DeutscheZierschrift.ttf"
        self.font = pygame.font.Font(font_path, 40)

        titulo = "Selecciona una cartass"

        draw_text(
                screen,
                titulo,
                self.font,
                col=(255,255,255),
                center=True,
                pos=(width//2, 50)
            )

        cartas = self.game.mazo

        inicio = self.scroll * self.columnas
        fin = inicio + self.filas_visibles * self.columnas
        visibles = cartas[inicio:fin]

        columnas_x = [
            width * 0.25,
            width * 0.5,
            width * 0.75
        ]

        for i, carta in enumerate(visibles):
            idx_real = inicio + i

            col = i % self.columnas
            fila = i // self.columnas

            x = columnas_x[col] - self.CARD_W // 2
            y = self.START_Y + fila * (self.CARD_H + self.ESP_Y)

            draw_card(screen, carta, x, y)

            if idx_real == self.selected:
                pygame.draw.rect(screen, (255,255,0), (x, y, self.CARD_W, self.CARD_H), 4)

        info = self.font.render(f"{self.selected+1}/{len(cartas)}", True, (255,255,255))
        screen.blit(info, (50, 40))