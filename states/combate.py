import pygame
import random
from Ui.FloatingText import FloatingText
from Ui.draw_cart import draw_card, draw_text, draw_options, draw_pocion
from Class.Utilities.Cofre import Cofre
from System.Save import guardar_juego


class CombatState:

    def __init__(self, game, carta_player, enemy=None, allow_exit=False):
        self.game = game
        self.player = carta_player
        self.enemy = enemy or Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()
        guardar_juego(self.game)

        if len(game.mazo) == 0:
            self.player = Cofre(random.choice(["C", "B", "A", "D"])).generar_carta()
            game.mazo.append(self.player)

        self.font = pygame.font.Font(None, 40)

        self.result_text = ""
        self.combate_terminado = False
        self.waiting_continue = False

        self.menu_state = "main"
        self.allow_exit = allow_exit
        self.selected_main = 0
        self.selected_sub = 0
        self.main_options = []
        self.update_main_options()

        self.float_texts = []
        self.delayed_events = []

        self.x_player = 300
        self.x_enemy = 500

        self.enemy_turn_delay = 0
        self.waiting_enemy = False

    def update_main_options(self):
        self.main_options = ["Atacar", "Inventario", "Cambiar carta"]
        if self.allow_exit:
            self.main_options.append("Salir")
        self.selected_main = min(self.selected_main, len(self.main_options) - 1)


    #  INPUT
    def handle_event(self, event):

        if event.type != pygame.KEYDOWN:
            return

        # 🏁 COMBATE TERMINADO (GANAR O PERDER)
        if self.combate_terminado:

            if event.key == pygame.K_RETURN:
                if self.waiting_continue and len(self.game.mazo) > 0:
                    from States.Selecc_Cart import SeleccionCartaState
                    self.game.change_state(
                        SeleccionCartaState(self.game, enemy=self.enemy, volver_a_combate=True)
                    )
                else:
                    from States.menu import MenuState
                    self.game.change_state(MenuState(self.game))

            elif event.key == pygame.K_ESCAPE:
                from States.menu import MenuState
                self.game.change_state(MenuState(self.game))

            return

        if self.menu_state == "main":
            if event.key == pygame.K_UP:
                self.selected_main = (self.selected_main - 1) % len(self.main_options)

            elif event.key == pygame.K_DOWN:
                self.selected_main = (self.selected_main + 1) % len(self.main_options)

            elif event.key == pygame.K_RETURN:
                self.select_main_option()

        elif self.menu_state == "atacar":
            habilidades = self.player.habilidades
            if event.key == pygame.K_UP:
                self.selected_sub = (self.selected_sub - 1) % len(habilidades)

            elif event.key == pygame.K_DOWN:
                self.selected_sub = (self.selected_sub + 1) % len(habilidades)

            elif event.key == pygame.K_RETURN:
                self.use_skill(self.selected_sub)

            elif event.key == pygame.K_ESCAPE:
                self.menu_state = "main"
                self.selected_sub = 0

        elif self.menu_state == "inventario":
            inventario = [item for item, cantidad in self.game.inventario.items() if cantidad > 0]
            inventario.append("Volver")

            if event.key == pygame.K_UP:
                self.selected_sub = (self.selected_sub - 1) % len(inventario)

            elif event.key == pygame.K_DOWN:
                self.selected_sub = (self.selected_sub + 1) % len(inventario)

            elif event.key == pygame.K_RETURN:
                seleccion = inventario[self.selected_sub]
                if seleccion == "Volver":
                    self.menu_state = "main"
                    self.selected_sub = 0
                else:
                    self.usar_pocion(seleccion, self.player)
                    self.menu_state = "main"
                    self.selected_sub = 0
                    if not self.combate_terminado:
                        self.enemy_turn()

            elif event.key == pygame.K_ESCAPE:
                self.menu_state = "main"
                self.selected_sub = 0

    #  COMBATE
    def select_main_option(self):
        opcion = self.main_options[self.selected_main]

        if opcion == "Atacar":
            self.menu_state = "atacar"
            self.selected_sub = 0

        elif opcion == "Inventario":
            self.menu_state = "inventario"
            self.selected_sub = 0

        elif opcion == "Cambiar carta":
            from States.Selecc_Cart import SeleccionCartaState
            self.game.change_state(SeleccionCartaState(self.game, enemy=self.enemy, volver_a_combate=False))

        elif opcion == "Salir":
            from States.menu import MenuState
            self.game.change_state(MenuState(self.game))

    def use_skill(self, index):

        if index >= len(self.player.habilidades):
            return

        resultado = self.player.usar_habilidad(index, self.enemy)

        if resultado.get("error"):
            self.result_text = f"Error: {resultado['error']}"
            self.menu_state = "main"
            self.selected_sub = 0
            return

        habilidad_nombre = resultado.get("habilidad", "Habilidad desconocida")
        efecto = resultado.get("resultado", {})

        self.result_text = f"{self.player.Characteristics.nombre} usa {habilidad_nombre}"

        self.apply_skill_effects(efecto)

        print("PLAYER_BUFFSTATUS: "+ self.player.Buff)
        print("PLAYER_DEBUFFSTATUS: "+ self.player.Debuff)
        print("ENMY_BUFFSTATUS: "+ self.enemy.Buff)
        print("ENMY_DEBUFFSTATUS: "+ self.enemy.Debuff)

        self.check_end()

        if not self.combate_terminado:
            self.enemy_turn_delay = 80  # ~0.6 segundos a 60 FPS
            self.waiting_enemy = True

        self.menu_state = "main"
        self.selected_sub = 0

    def apply_skill_effects(self, resultado):
        if "damage" in resultado:
            damage = resultado["damage"]
            if isinstance(damage, int):
                self.enemy.anim_state = "hurt"
                self.enemy.anim_timer = 15
                self.float_texts.append(FloatingText(f"-{damage}", self.x_enemy, 200, (255,80,80)))

        if "total_damage" in resultado:
            total = resultado["total_damage"]
            self.enemy.anim_state = "hurt"
            self.enemy.anim_timer = 15
            self.float_texts.append(FloatingText(f"-{total}", self.x_enemy, 200, (255,80,80)))

        if "hit" in resultado:
            self.enemy.anim_state = "hurt"
            self.enemy.anim_timer = 15
            self.float_texts.append(FloatingText("HIT", self.x_enemy, 200, (255,255,255)))

        if "heal" in resultado:
            heal = resultado["heal"]
            self.player.anim_state = "heal"
            self.player.anim_timer = 20
            self.float_texts.append(FloatingText(f"+{heal}", self.x_player, 200, (80,255,120)))

        if "steal" in resultado:
            steal = resultado["steal"]
            self.float_texts.append(FloatingText(f"+{steal}", self.x_player, 200, (80,255,120)))

        if "debuff" in resultado and resultado["debuff"]:
            self.float_texts.append(FloatingText("Debuff", self.x_enemy, 200, (200,100,100)))

    def enemy_turn(self):

        if self.combate_terminado:
            return

        import random

        habilidad = random.choice(self.enemy.habilidades)

        resultado = habilidad.usar(self.enemy, self.player)

        if resultado.get("error"):
            return

        self.result_text = f"El enemigo usa {habilidad.nombre}"

        self.apply_enemy_effects(resultado)

        self.check_end()

    def get_x(self, carta):
        return self.x_player if carta == self.player else self.x_enemy


    def handle_Regenerator_heal(self):
        for carta, x in [(self.player, self.x_player), (self.enemy, self.x_enemy)]:
            if getattr(carta, "nombre", "") == "Regenerator":
                heal = int(carta.HP * 0.1)
                carta.Heal(heal)
                self.float_texts.append(FloatingText(f"+{heal}", x, 200, (80,255,120)))

    def check_end(self):

        if self.enemy.HP <= 0:
            from States.victory import VictoryState
            recompensa = Cofre(random.choice(["C", "B", "A", "D"])).generar_contenido()
            self.player.restore_stats()
            self.game.change_state(
                VictoryState(self.game, self.player, self.enemy, recompensa)
            )

        elif self.player.HP <= 0:
            if self.player in self.game.mazo:
                self.game.mazo.remove(self.player)

            guardar_juego(self.game)

            if len(self.game.mazo) > 0:
                from States.Selecc_Cart import SeleccionCartaState
                self.game.change_state(
                    SeleccionCartaState(self.game, enemy=self.enemy, volver_a_combate=True)
                )
            else:
                self.combate_terminado = True
                self.waiting_continue = True
                self.result_text = "Perdiste!"

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

        if self.waiting_enemy:
            self.enemy_turn_delay -= 1

            if self.enemy_turn_delay <= 0:
                self.enemy_turn()
                self.waiting_enemy = False
    

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


    def draw(self, screen):

        screen.fill((30, 30, 30))
        width = screen.get_width()

        font_path = "./Ui/fonts/EnchantedLand.otf"
        font_ui = pygame.font.Font(font_path, 20)
        

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

        self.draw_menu(screen, width, font_ui)

        for t in self.float_texts:
            t.draw(screen)

        items = list(self.game.inventario.items())
        espacios_ocupados = 0  

        for item, cantidad in items:
            if cantidad > 0:
                pos_x = 50 + espacios_ocupados * 60
                draw_pocion(screen, item, pos_x, 20, cantidad)
                espacios_ocupados += 1

    def draw_menu(self, screen, width, font_ui):

        height = screen.get_height()

        # 📐 Caja del menú (centrada)
        box_w = width * 0.5
        box_h = (height * 0.15)+5
        box_x = (width - box_w) / 2
        box_y = height * 0.65

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (box_x, box_y, box_w, box_h),
            4,
            border_radius=15
        )

        # 📍 grid dinámico (2 columnas)
        cols = 2
        spacing_x = box_w / cols
        spacing_y = 60

        start_x = box_x
        start_y = box_y + 20

        def get_pos(i):
            col = i % cols
            row = i // cols
            x = start_x + col * spacing_x + 20
            y = start_y + row * spacing_y
            return (x, y)

        # -------------------------
        # 🧭 MENÚ PRINCIPAL
        # -------------------------
        if self.menu_state == "main":

            draw_text(screen, "MENÚ", font_ui, col=(255,255,255), pos=(width//2, box_y - 40), center=True)

            for i, option in enumerate(self.main_options):
                color = (255, 255, 0) if i == self.selected_main else (255, 255, 255)
                x, y = get_pos(i)
                draw_options(screen, x, y)
                draw_text(screen, option, font_ui, col=color, pos=get_pos(i))

            

            draw_text(
                screen,
                "ENTER = seleccionar | ↑↓ = navegar",
                font_ui,
                col=(180,180,180),
                pos=(box_x, box_y + box_h + 10)
            )

        # -------------------------
        # ⚔️ HABILIDADES
        # -------------------------
        elif self.menu_state == "atacar":

            draw_text(screen, "Habilidades", font_ui, col=(255,255,255), pos=(width//2, box_y - 40), center=True)

            for i, habilidad in enumerate(self.player.habilidades):

                color = (255, 255, 0) if i == self.selected_sub else (255, 255, 255)
                
                # 🔥 opcional: deshabilitar si no hay MP
                if hasattr(habilidad, "MP") and self.player.MP < habilidad.MP:
                    color = (120, 120, 120)

                texto = f"{habilidad.nombre}"
                x, y = get_pos(i)
                draw_options(screen, x, y, habilidad)
                draw_text(screen, texto, font_ui, col=color, pos=get_pos(i))

            draw_text(screen, "ESC = volver", font_ui, col=(180,180,180), pos=(box_x, box_y + box_h + 10))
            draw_text(screen, f"MP: {self.player.MP}/{self.player.Base_MP}", font_ui, col=(180,180,180), pos=(box_x + 250, box_y + box_h + 10))

        # -------------------------
        # 🎒 INVENTARIO
        # -------------------------
        elif self.menu_state == "inventario":

            draw_text(screen, "Inventario", font_ui, col=(255,255,255), pos=(width//2, box_y - 40), center=True)

            inventario = [item for item, cantidad in self.game.inventario.items() if cantidad > 0]
            inventario.append("Volver")

            for i, item in enumerate(inventario):

                color = (255, 255, 0) if i == self.selected_sub else (255, 255, 255)

                if item != "Volver":
                    cantidad = self.game.inventario.get(item, 0)
                    text = f"{item} x{cantidad}"
                else:
                    text = item

                draw_text(screen, text, font_ui, col=color, pos=get_pos(i))

            draw_text(screen, "ENTER = usar", font_ui, col=(180,180,180), pos=(box_x, box_y + box_h + 10))
            draw_text(screen, "ESC = volver", font_ui, col=(180,180,180), pos=(box_x + 250, box_y + box_h + 10))

    def apply_enemy_effects(self, resultado):

        if "damage" in resultado:
            damage = resultado["damage"]
            self.player.anim_state = "hurt"
            self.player.anim_timer = 15
            self.float_texts.append(FloatingText(f"-{damage}", self.x_player, 200, (255,80,80)))

        if "total_damage" in resultado:
            total = resultado["total_damage"]
            self.player.anim_state = "hurt"
            self.player.anim_timer = 15
            self.float_texts.append(FloatingText(f"-{total}", self.x_player, 200, (255,80,80)))

        if "heal" in resultado:
            heal = resultado["heal"]
            self.enemy.anim_state = "heal"
            self.enemy.anim_timer = 20
            self.float_texts.append(FloatingText(f"+{heal}", self.x_enemy, 200, (80,255,120)))

        if "debuff" in resultado:
            self.float_texts.append(FloatingText("Debuff", self.x_player, 200, (200,100,100)))

    def add_delayed_event(self, delay, func):
        self.delayed_events.append({"timer": delay, "func": func})