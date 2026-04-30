import pygame
import random
from Ui.FloatingText import FloatingText
from Ui.draw_cart import draw_card, draw_options, draw_text, draw_item, draw_pocion
from design.Cofre import Cofre
from system.Save import guardar_juego


class CombatState:

    def __init__(self, game, carta_player, enemy=None):
        self.game = game
        self.player = carta_player
        self.enemy = enemy or Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()

        if len(game.mazo) == 0:
            self.player = Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()
            game.mazo.append(self.player)

        self.font = pygame.font.Font(None, 40)

        self.options = ["Piedra", "Papel", "Tijera"]

        self.result_text = ""
        self.combate_terminado = False
        self.waiting_continue = False

        self.selected_player = None
        self.selected_enemy = None

        self.float_texts = []
        self.delayed_events = []

        self.x_player = 300
        self.x_enemy = 500

    # -------------------------
    # 🎮 INPUT
    # -------------------------
    def handle_event(self, event):

        if event.type != pygame.KEYDOWN:
            return

        # 🏁 COMBATE TERMINADO (GANAR O PERDER)
        if self.combate_terminado:

            if event.key == pygame.K_RETURN:

                # 🔴 SI PERDISTE → elegir carta
                if self.waiting_continue and len(self.game.mazo) > 0:
                    from states.Selecc_Cart import SeleccionCartaState
                    self.game.change_state(
                        SeleccionCartaState(self.game, enemy=self.enemy)
                    )

                else:
                    from states.menu import MenuState
                    self.game.change_state(MenuState(self.game))

            elif event.key == pygame.K_ESCAPE:
                from states.menu import MenuState
                self.game.change_state(MenuState(self.game))

            return

        # 🎮 INPUT NORMAL
        if event.key == pygame.K_1:
            self.selected_player = 0
            self.turno("Piedra")

        elif event.key == pygame.K_2:
            self.selected_player = 1
            self.turno("Papel")

        elif event.key == pygame.K_3:
            self.selected_player = 2
            self.turno("Tijera")

        if event.key == pygame.K_q:
            self.usar_pocion("Minipocion", self.player)

        elif event.key == pygame.K_w:
            self.usar_pocion("Pocion", self.player)

        elif event.key == pygame.K_e:
            self.usar_pocion("Superpocion", self.player)

        elif event.key == pygame.K_r:
            self.usar_pocion("Hiperpocion", self.player)

    # -------------------------
    # ⚔️ COMBATE
    # -------------------------
    def turno(self, eleccion):

        if self.waiting_continue or self.combate_terminado:
            return

        enemigo = random.choice(self.options)
        self.selected_enemy = self.options.index(enemigo)

        if eleccion == enemigo:
            self.result_text = "Empate"
            self.handle_Regenerator_heal()
            return

        win = (
            (eleccion == "Piedra" and enemigo == "Tijera") or
            (eleccion == "Papel" and enemigo == "Piedra") or
            (eleccion == "Tijera" and enemigo == "Papel")
        )

        if win:
            self.atacar(self.player, self.enemy, self.x_enemy)
            self.result_text = "Golpeas!"
        else:
            self.atacar(self.enemy, self.player, self.x_player)
            self.result_text = "Te golpean!"

        self.check_end()

    # -------------------------
    # 💥 ATAQUE
    # -------------------------
    def atacar(self, atacante, objetivo, x_pos):

        ataque = atacante.Atacar()
        resultado = objetivo.Recibir_daño(ataque)

        objetivo.anim_timer = 15

        if resultado == "miss":
            objetivo.anim_state = "miss"
            self.float_texts.append(FloatingText("MISS", x_pos, 200, (255,255,255)))

        else:
            objetivo.anim_state = "hurt"
            self.float_texts.append(FloatingText(f"-{int(ataque)}", x_pos, 200, (255,80,80)))

            if resultado == "Charged":
                self.add_delayed_event(20, lambda:
                    self.float_texts.append(FloatingText("Cargando", x_pos, 200, (255,255,80)))
                )

        if objetivo.nombre == "Dragon":
            daño = ataque * 0.1
            atacante.Recibir_daño(daño)
            self.float_texts.append(FloatingText(f"-{int(daño)}", self.get_x(atacante), 200, (255,80,80)))

        if atacante.nombre == "Drain":
            heal = ataque * 0.25
            atacante.Recuperar_vida(heal)
            self.float_texts.append(FloatingText(f"+{int(heal)}", self.get_x(atacante), 200, (80,255,120)))

    def get_x(self, carta):
        return self.x_player if carta == self.player else self.x_enemy

    # -------------------------
    # 🧪 EFECTOS
    # -------------------------
    def handle_Regenerator_heal(self):

        for carta, x in [(self.player, self.x_player), (self.enemy, self.x_enemy)]:
            if carta.nombre == "Regenerator":
                heal = carta.vida * 0.1
                carta.Recuperar_vida()
                self.float_texts.append(FloatingText(f"+{int(heal)}", x, 200, (80,255,120)))

    # -------------------------
    # 🏁 FIN
    # -------------------------
    def check_end(self):

        if self.enemy.vida <= 0:

            from states.victory import VictoryState
            recompensa = Cofre(random.choice(["C", "B", "A", "D"])).generar_contenido()
            self.player.victori()
            self.game.change_state(
                VictoryState(self.game, self.player, self.enemy, recompensa)
            )
            

        elif self.player.vida <= 0:
            self.combate_terminado = True
            self.waiting_continue = True  
            self.result_text = "Perdiste!"

            if self.player in self.game.mazo:
                self.game.mazo.remove(self.player)

            guardar_juego(self.game)

    # -------------------------
    # 🔄 UPDATE
    # -------------------------
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

        for e in self.delayed_events:
            e["timer"] -= 1
            if e["timer"] <= 0:
                e["func"]()

        self.delayed_events = [e for e in self.delayed_events if e["timer"] > 0]
    

    def usar_pocion(self, pocion, carta):

        # validar existencia
        if pocion not in self.game.inventario:
            return

        if self.game.inventario[pocion] <= 0:
            return

        heal=carta.Pocion_Use(pocion)

        # consumir
        self.game.inventario[pocion] -= 1

        # feedback visual
        self.float_texts.append(
            FloatingText(f"+{heal}", self.get_x(carta), 200, (80,255,120))
        )

        carta.anim_state = "heal"
        carta.anim_timer = 20

    # -------------------------
    # 🎨 DRAW
    # -------------------------
    def draw(self, screen):

        screen.fill((30, 30, 30))
        width = screen.get_width()

        font_path = "./Ui/fonts/DeutscheZierschrift.ttf"
        font_ui = pygame.font.Font(font_path, 40)
        

        draw_text(screen, self.result_text, font_ui, center=True, pos=(width//2, 50))


        if self.combate_terminado:

            if self.waiting_continue:
                draw_text(screen, "ENTER continuar | ESC salir",
                          font_ui, center=True, pos=(width//2, 750))
            else:
                draw_text(screen, "ENTER o ESC para volver al menú",
                          font_ui, center=True, pos=(width//2, 750))

        self.x_player = width * 0.25
        self.x_enemy = width * 0.75

        draw_card(screen, self.player, self.x_player - 100, 150)
        draw_card(screen, self.enemy, self.x_enemy - 100, 150)

        for i, op in enumerate(self.options):
            offset = -30 if self.selected_player == i else 0
            draw_options(screen, op, 120 + i * 90, 480, offset, player=True)

        for i, op in enumerate(self.options):
            offset = -30 if self.selected_enemy == i else 0
            draw_options(screen, op, 620 + i * 90, 480, offset)

        for t in self.float_texts:
            t.draw(screen)


        #pociones
        items = list(self.game.inventario.items())
        espacios_ocupados = 0  

        for item, cantidad in items:
            if cantidad > 0:
                
                pos_x = 50 + espacios_ocupados * 60
                draw_pocion(screen, item, pos_x, 20, cantidad)
                
                espacios_ocupados += 1


           

    

    
    def add_delayed_event(self, delay, func):
        self.delayed_events.append({"timer": delay, "func": func})