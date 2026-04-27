import pygame
from Ui.draw_cart import draw_card, draw_text

class MazoState:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 40)

        self.scroll = 0
        self.columnas = 3
        self.filas_visibles = 2

        self.CARD_W, self.CARD_H = 200, 300
        self.ESP_X, self.ESP_Y = 20, 20
        self.START_X, self.START_Y = 100, 120

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                self.scroll += 1

            elif event.key == pygame.K_UP:
                self.scroll = max(0, self.scroll - 1)

            elif event.key == pygame.K_ESCAPE:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((20, 20, 20))

        width = screen.get_width()

        # Título centrado
        font_path = "./Ui/fonts/DeutscheZierschrift.ttf"
        self.font = pygame.font.Font(font_path, 40)

        titulo = "Mazo"

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

        # 📌 posiciones de columnas (1/4, 2/4, 3/4)
        columnas_x = [
            width * 0.25,
            width * 0.5,
            width * 0.75
        ]

        for i, carta in enumerate(visibles):
            col = i % self.columnas
            fila = i // self.columnas

            x = columnas_x[col] - self.CARD_W // 2
            y = self.START_Y + fila * (self.CARD_H + self.ESP_Y)

            draw_card(screen, carta, x, y)

        # indicador de scroll
        info = self.font.render(f"{inicio+1}-{min(fin, len(cartas))}/{len(cartas)}", True, (255,255,255))
        screen.blit(info, (50, 40))