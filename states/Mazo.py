import pygame
from Ui.draw_cart import draw_card, draw_text, font_ui, font_ui_mini
from design.Cofre import Cofre


class MazoState:
    def __init__(self, game):
        self.game = game

        self.scroll = 0
        self.columnas = 3
        self.filas_visibles = 2

        self.CARD_W, self.CARD_H = 200, 300
        self.ESP_Y = 20
        self.START_Y = 120

        self.selected = 0
        self.show_info = False
        self.show_menu = False
        self.menu_selected = 0

        # 🎬 animación
        self.anim_scale = 1
        self.anim_target = 1
        
        # Mensaje temporal
        self.mensaje = None
        self.mensaje_timer = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            
            # Si hay un menú abierto
            if self.show_menu:
                if event.key == pygame.K_UP:
                    self.menu_selected = (self.menu_selected - 1) % 2
                elif event.key == pygame.K_DOWN:
                    self.menu_selected = (self.menu_selected + 1) % 2
                elif event.key == pygame.K_RETURN:
                    self.ejecutar_accion_menu()
                elif event.key == pygame.K_ESCAPE:
                    self.show_menu = False
                    self.menu_selected = 0
            else:
                if event.key == pygame.K_RIGHT:
                    self.selected = min(self.selected + 1, len(self.game.mazo) - 1)

                elif event.key == pygame.K_LEFT:
                    self.selected = max(self.selected - 1, 0)

                elif event.key == pygame.K_DOWN:
                    self.selected = min(self.selected + self.columnas, len(self.game.mazo) - 1)

                elif event.key == pygame.K_UP:
                    self.selected = max(self.selected - self.columnas, 0)

                elif event.key == pygame.K_RETURN:
                    self.show_menu = True
                    self.menu_selected = 0
                    self.anim_scale = 0.8

                elif event.key == pygame.K_ESCAPE:
                    from states.menu import MenuState
                    self.game.change_state(MenuState(self.game))

    def ejecutar_accion_menu(self):
        """Ejecuta la acción del menú seleccionado"""
        if self.menu_selected == 0:
            self.show_info = not self.show_info
            self.show_menu = False
        elif self.menu_selected == 1:
            self.vender_carta()

    def vender_carta(self):
        """Vende la carta seleccionada"""
        if len(self.game.mazo) > 0:
            carta = self.game.mazo[self.selected]
            valor = carta.obtener_valor_venta()
            rango = carta.obtener_rango_venta()
            
            self.game.oro += valor
            self.game.mazo.pop(self.selected)
            
            # Ajustar selección si es necesario
            if self.selected >= len(self.game.mazo) and self.selected > 0:
                self.selected -= 1
            
            # Guardar el juego
            from system.Save import guardar_juego
            guardar_juego(self.game)
            
            self.mensaje = f"¡Vendiste {carta.nombre} ({rango}) por {valor} oro!"
            self.mensaje_timer = 120
            
            self.show_menu = False

    def update(self):
        # 🎬 animación suave
        self.anim_scale += (1 - self.anim_scale) * 0.15
        
        if self.mensaje_timer > 0:
            self.mensaje_timer -= 1

    def draw(self, screen):
        screen.fill((20, 20, 20))
        width = screen.get_width()
        height = screen.get_height()

        draw_text(screen, "Mazo", font_ui, center=True, pos=(width//2, 50))
        
        if not self.show_menu:
            draw_text(screen, "[ENTER] Opciones    [ESC] Salir", font_ui_mini, center=True, pos=(width//2, 750))
        else:
            draw_text(screen, "[ENTER] Confirmar    [ESC] Cancelar", font_ui_mini, center=True, pos=(width//2, 750))

        cartas = self.game.mazo

        columnas_x = [width * 0.25, width * 0.5, width * 0.75]

        for i, carta in enumerate(cartas):
            col = i % self.columnas
            fila = i // self.columnas

            x = columnas_x[col] - self.CARD_W // 2
            y = self.START_Y + fila * (self.CARD_H + self.ESP_Y)

            seleccionado = (i == self.selected)

            # 🎬 animación solo en la seleccionada
            scale = self.anim_scale if seleccionado else 1

            draw_card(
                screen,
                carta,
                x,
                y,
                info=(seleccionado and self.show_info),
                scale=scale
            )
            
            # Resalte de carta seleccionada (rectángulo amarillo)
            if seleccionado:
                pygame.draw.rect(screen, (255, 255, 0), (x, y, self.CARD_W, self.CARD_H), 4)
        
        # Dibujar menú si está abierto
        if self.show_menu:
            self.draw_menu(screen, width, height)
        
        # Dibujar mensaje temporal
        if self.mensaje and self.mensaje_timer > 0:
            draw_text(screen, self.mensaje, font_ui_mini, col=(100, 255, 100), center=True, pos=(width//2, 650))
    
    def draw_menu(self, screen, width, height):
        """Dibuja el menú de opciones"""
        if len(self.game.mazo) == 0:
            return
        
        carta = self.game.mazo[self.selected]
        valor = carta.obtener_valor_venta()
        
        # Fondo oscuro
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Opciones
        opciones = ["Ver Info", f"Vender ({valor} oro)"]
        
        # Dibujar opciones
        menu_height = len(opciones) * 60
        menu_y = height // 2 - menu_height // 2
        
        draw_text(screen, f"Selecciona una acción para {carta.nombre}:", font_ui_mini, center=True, pos=(width//2, menu_y - 60))
        
        for i, opcion in enumerate(opciones):
            y = menu_y + i * 60
            color = (100, 255, 100) if i == self.menu_selected else (255, 255, 255)
            marker = ">>> " if i == self.menu_selected else "    "
            draw_text(screen, marker + opcion, font_ui_mini, col=color, center=True, pos=(width//2, y))