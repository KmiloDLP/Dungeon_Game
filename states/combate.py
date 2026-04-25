import pygame
import random
from Ui.draw_cart import draw_card
from design.Cofre import Cofre
from system.Save import guardar_juego
from cartas.Lichs import Lichs


class CombatState:

    def __init__(self, game, carta_player, enemy=None):
        self.combate_terminado = False
        self.game = game
        self.player = carta_player
        self.font = pygame.font.Font(None, 40) 

        # enemigo
        if enemy:
            self.enemy = enemy
        else:
            self.enemy = Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()
    
        # jugador
        if len(game.mazo) == 0:
            self.player = Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()
            game.mazo.append(self.player)

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

            if self.enemy.nombre == "Troll":
                self.enemy.Recuperar_vida()

            if self.player.nombre == "Troll":
                self.player.Recuperar_vida()
                
            return

        win = (
            (eleccion == "Piedra" and enemigo == "Tijera") or
            (eleccion == "Papel" and enemigo == "Piedra") or
            (eleccion == "Tijera" and enemigo == "Papel")
        )

        if win:

            ataque = self.player.Atacar()
            self.enemy.Recibir_daño(ataque)

            if self.enemy.nombre == "Dragon":
                self.player.Recibir_daño(ataque * 0.1)

            self.result_text = "Golpeas!"
        else:

            ataque = self.enemy.Atacar()
            self.player.Recibir_daño(ataque)

            if self.player.nombre == "Dragon":
                self.enemy.Recibir_daño(ataque * 0.1)


            self.result_text = "Te golpean!"

        self.check_end()

    def check_end(self):

        if self.enemy.vida <= 0:

            print("Enemy defeated!")
            self.combate_terminado = True
            recompensa = Cofre(random.choice(["C", "B", "A", "D"])).generar_contenido()

            print("Recompensa obtenida:", recompensa)

            if isinstance(recompensa, int):
                self.game.oro += recompensa
            elif isinstance(recompensa, str):
                if recompensa in self.game.inventario:
                    self.game.inventario[recompensa] += 1
                else:
                    self.game.inventario[recompensa] = 1
            else:
                self.game.mazo.append(recompensa)

            self.player.vida = self.player.vida_max

            self.result_text = "Ganaste!"
            guardar_juego(self.game)
        
        elif self.player.vida <= 0:
            self.combate_terminado = True

            self.game.mazo.remove(self.player)
            self.result_text = "Perdiste!"
            guardar_juego(self.game)

            if len(self.game.mazo) > 0:
                from states.Selecc_Cart import SeleccionCartaState
                self.game.change_state(SeleccionCartaState(self.game, enemy=self.enemy)
)
            else:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 30))

        width = screen.get_width()

        texto = self.font.render(self.result_text, True, (255,255,255))
        screen.blit(texto, (width//2 - texto.get_width()//2, 50))

        x_player = width * 0.25
        x_enemy = width * 0.75

        CARD_W = 200  

        draw_card(screen, self.player, x_player - CARD_W//2, 150)
        draw_card(screen, self.enemy, x_enemy - CARD_W//2, 150)

        # Opciones
        for i, op in enumerate(self.options):
            txt = self.font.render(f"{i+1}. {op}", True, (255,255,255))
            screen.blit(txt, (100, 450 + i * 40))