from turtle import width

import pygame
import random
from Ui.FloatingText import FloatingText
from Ui.draw_cart import draw_card, draw_options, draw_text
from design.Cofre import Cofre
from system.Save import guardar_juego


class CombatState:

    def __init__(self, game, carta_player, enemy=None):
        self.combate_terminado = False
        self.game = game
        self.player = carta_player
        self.font = pygame.font.Font(None, 40) 
        self.float_texts = []
        self.delayed_events = []

        self.x_player = 300
        self.selected_player = None
        self.x_enemy = 500
        self.selected_enemy = None  

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
            if   event.key == pygame.K_1:
                self.turno("Piedra")
                self.selected_player = 0
            elif event.key == pygame.K_2:
                self.turno("Papel")
                self.selected_player = 1
            elif event.key == pygame.K_3:
                self.selected_player = 2
                self.turno("Tijera")

   
    def turno(self, eleccion):

        if self.combate_terminado:

            print("Combate terminado, presiona Enter para volver al menú")
            return
        
        enemigo = random.choice(self.options)
        self.selected_enemy = self.options.index(enemigo)

        if eleccion == enemigo:
            self.result_text = "Empate"

            if self.enemy.nombre == "Troll":
                self.enemy.Recuperar_vida()

                self.float_texts.append(
                    FloatingText(f"+{int(self.enemy.vida * 0.1)}", self.x_enemy, 200, (80, 255, 120))
                )

            if self.player.nombre == "Troll":
                self.player.Recuperar_vida()
                self.float_texts.append(
                    FloatingText(f"+{int(self.player.vida * 0.1)}", self.x_player, 200, (80, 255, 120))
                )
                
            return

        win = (
            (eleccion == "Piedra" and enemigo == "Tijera") or
            (eleccion == "Papel" and enemigo == "Piedra") or
            (eleccion == "Tijera" and enemigo == "Papel")
        )

        if win:

            ataque = self.player.Atacar()
            resultado = self.enemy.Recibir_daño(ataque)

            self.enemy.anim_timer = 15
            

            if resultado == "miss":
                self.enemy.anim_state = "miss"

                self.float_texts.append(
                    FloatingText("MISS", self.x_enemy, 200, (255, 255, 255))
                )
            elif resultado == "Charged":

                self.enemy.anim_state = "hurt"

                self.float_texts.append(
                    FloatingText(f"-{int(ataque)}", self.x_enemy, 200, (255, 80, 80))
                )
                self.add_delayed_event(20, lambda: self.float_texts.append(
                    FloatingText("Cargando", self.x_enemy, 200, (255, 255, 80))
                ))

            else:
                self.enemy.anim_state = "hurt"

                self.float_texts.append(
                   FloatingText(f"-{int(ataque)}", self.x_enemy, 200, (255, 80, 80))
                )
     

            if self.enemy.nombre == "Dragon":
                self.player.Recibir_daño(ataque * 0.1)
                self.float_texts.append(
                    FloatingText(f"-{int(ataque * 0.1)}", self.x_player, 200, (255, 80, 80))
                )
            
            if self.player.nombre == "Vampiro":
                self.player.Recuperar_vida(ataque)
                self.float_texts.append(
                    FloatingText(f"+{int(ataque * 0.25)}", self.x_player, 200, (80, 255, 120))
                )

            self.result_text = "Golpeas!"
        else:

            ataque = self.enemy.Atacar()
            resultado = self.player.Recibir_daño(ataque)
            self.player.anim_timer = 15

           

            if resultado == "miss":
                self.player.anim_state = "miss"

                self.float_texts.append(
                    FloatingText("MISS", self.x_player, 200, (255, 255, 255))
                )
            elif resultado == "Charged":

                self.player.anim_state = "hurt"

                self.float_texts.append(
                    FloatingText(f"-{int(ataque)}", self.x_player, 200, (255, 80, 80))
                )
                self.add_delayed_event(20, lambda: self.float_texts.append(
                    FloatingText("Cargando", self.x_player, 200, (255, 255, 80))
                ))
            else:
                self.player.anim_state = "hurt"

                self.float_texts.append(
                   FloatingText(f"-{int(ataque)}", self.x_player, 200, (255, 80, 80))
                )

            if self.player.nombre == "Dragon":
                self.enemy.Recibir_daño(ataque * 0.1)
                self.float_texts.append(
                    FloatingText(f"-{int(ataque * 0.1)}", self.x_enemy, 200, (255, 80, 80))
                ) 

            if self.enemy.nombre == "Vampiro":
                self.enemy.Recuperar_vida(ataque)
                self.float_texts.append(
                    FloatingText(f"+{int(ataque * 0.25)}", self.x_enemy, 200, (80, 255, 120))
                )

            self.result_text = "Te golpean!"

        self.check_end()

    def check_end(self):

        if self.enemy.vida <= 0:

            
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
        for carta in [self.player, self.enemy]:

            if carta.anim_timer > 0:
                carta.anim_timer -= 1

            if carta.shake > 0:
                carta.shake -= 1

            if carta.anim_timer <= 0 and carta.shake <= 0:
                carta.anim_state = "idle"

        for t in self.float_texts:
            t.update()

        self.float_texts = [t for t in self.float_texts if t.alive()]

        for event in self.delayed_events:
            event["timer"] -= 1

            if event["timer"] <= 0:
                event["func"]()

        self.delayed_events = [e for e in self.delayed_events if e["timer"] > 0]

    def draw(self, screen):
        screen.fill((30, 30, 30))

        width = screen.get_width()

        font= "./Ui/fonts/DeutscheZierschrift.ttf" 
        font_anunce = pygame.font.Font(font, 40)


        draw_text(screen,  self.result_text, font_anunce, center=True, pos=(width//2, 50))
        if self.result_text == "Ganaste!":
            draw_text(screen, "Presiona Enter para volver al menu", font_anunce, center=True, pos=(width//2, 750))


        self.x_player = width * 0.25
        self.x_enemy = width * 0.75

        CARD_W = 200  

        draw_card(screen, self.player, self.x_player - CARD_W//2, 150)
        draw_card(screen, self.enemy, self.x_enemy - CARD_W//2, 150)

        for i, op in enumerate(self.options):
            offset = 0
            if self.selected_player == i:
                offset = -30  # 👈 sube 20px
            draw_options(screen, op, 120 + i * 90, 500, offset)
            
        for i, op in enumerate(self.options):
            offset = 0
            if self.selected_enemy == i:
                offset = -30  # 👈 sube 20px
            draw_options(screen, op, 620 + i * 90, 500, offset)


        for t in self.float_texts:
            t.draw(screen)

    def add_delayed_event(self, delay, func):

        self.delayed_events.append({
            "timer": delay,
            "func": func
        })