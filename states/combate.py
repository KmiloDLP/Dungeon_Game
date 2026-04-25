import pygame
import random
from Ui.draw_cart import draw_card
from design.Cofre import Cofre


class CombatState:
    def __init__(self, game):
        self.combate_terminado = False
        self.game = game
        self.font = pygame.font.Font(None, 40)
    
        self.enemy = Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()

        # jugador
        if len(game.mazo) == 0:
            self.player = Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()
            game.mazo.append(self.player)
        else:
            self.player = game.mazo[0]

        self.options = ["Piedra", "Papel", "Tijera"]
        self.result_text = ""

    def handle_event(self, event):

        if self.combate_terminado:
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))
            return


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.turno("Piedra")
            elif event.key == pygame.K_2:
                self.turno("Papel")
            elif event.key == pygame.K_3:
                self.turno("Tijera")

    def turno(self, eleccion):

        if self.combate_terminado:
            print("Combate terminado, presiona Enter para volver al menú")
            return
        
        enemigo = random.choice(self.options)

        if eleccion == enemigo:
            self.result_text = "Empate"
            return

        win = (
            (eleccion == "Piedra" and enemigo == "Tijera") or
            (eleccion == "Papel" and enemigo == "Piedra") or
            (eleccion == "Tijera" and enemigo == "Papel")
        )

        if win:
            self.enemy.Recibir_daño(self.player.atk)
            self.result_text = "Golpeas!"
        else:
            self.player.Recibir_daño(self.enemy.atk)
            self.result_text = "Te golpean!"

        self.check_end()

    def check_end(self):

        print("chequeo")

        if self.enemy.vida <= 0:

            print("Enemy defeated!")
            self.combate_terminado = True
            recompensa = Cofre(random.choice(["C", "B", "A", "D"])).generar_contenido()

            print("Recompensa obtenida:", recompensa)

            if isinstance(recompensa, int):
                self.game.oro += recompensa
            elif isinstance(recompensa, str):
                self.game.inventario.append(recompensa)
            else:
                self.game.mazo.append(recompensa)
                print("Mazo:", self.game.mazo)

            self.result_text = "Ganaste!"
        
        elif self.player.vida <= 0:
            self.combate_terminado = True

            self.game.mazo.remove(self.player)
            self.result_text = "Perdiste!"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 30))

        # 📝 resultado del turno
        texto = self.font.render(self.result_text, True, (255,255,255))
        screen.blit(texto, (300, 50))

        # 🎴 dibujar cartas
        draw_card(screen, self.player, 100, 150)
        draw_card(screen, self.enemy, 500, 150)

        # 🎮 opciones
        for i, op in enumerate(self.options):
            txt = self.font.render(f"{i+1}. {op}", True, (255,255,255))
            screen.blit(txt, (100, 450 + i * 40))