import pygame
import random
from Ui.draw_cart import draw_item, draw_text, font_ui, font_ui_mini
from Class.Utilities.Cofre import Cofre

class InventarioState:
    def __init__(self, game):
        self.game = game

        self.selected = 0
        self.show_info = False
        self.show_menu = False
        self.menu_selected = 0

        self.columnas = 4

        # 🎬 animación
        self.anim_scale = 1
        
        # Mensaje temporal
        self.mensaje = None
        self.mensaje_timer = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            
            # Si hay un menú abierto
            if self.show_menu:
                if event.key == pygame.K_UP:
                    self.menu_selected = 0 if self.menu_selected == 1 else 1
                elif event.key == pygame.K_DOWN:
                    self.menu_selected = 1 if self.menu_selected == 0 else 0
                elif event.key == pygame.K_RETURN:
                    self.ejecutar_accion_menu()
                elif event.key == pygame.K_ESCAPE:
                    self.show_menu = False
                    self.menu_selected = 0
            else:
                if event.key == pygame.K_RIGHT:
                    self.selected += 1

                elif event.key == pygame.K_LEFT:
                    self.selected -= 1

                elif event.key == pygame.K_DOWN:
                    self.selected += self.columnas

                elif event.key == pygame.K_UP:
                    self.selected -= self.columnas

                elif event.key == pygame.K_RETURN:
                    items = self.get_items()
                    item_name = items[self.selected][0]
                    if item_name == "Oro":
                        return
                    self.show_info = not self.show_info
                    if not self.show_info:
                        self.abrir_menu()
                    self.anim_scale = 0.8

                elif event.key == pygame.K_ESCAPE:
                    from States.menu import MenuState
                    self.game.change_state(MenuState(self.game))

        total = len(self.get_items())
        self.selected = max(0, min(self.selected, total - 1))

    def get_items(self):
        items = [("Oro", self.game.oro)] + list(self.game.inventario.items())
        # Agregar Tienda al final
        items.append(("Tienda", 200))
        return items
    
    def abrir_menu(self):
        """Abre el menú de opciones para el item seleccionado"""
        items = self.get_items()
        item_name = items[self.selected][0]
        
        if item_name == "Oro":
            return
        
        self.show_menu = True
        self.menu_selected = 0

    def ejecutar_accion_menu(self):
        """Ejecuta la acción del menú seleccionado"""
        items = self.get_items()
        item_name = items[self.selected][0]
        
        if item_name == "Tienda":
            self.comprar_en_tienda()
        else:
            # Para pociones u otros items
            if self.menu_selected == 0:
                self.mostrar_info_item(item_name)
            elif self.menu_selected == 1:
                self.usar_item(item_name)
    
    def comprar_en_tienda(self):
        """Compra una carta aleatoria por 200 de oro"""
        if self.game.oro >= 200:
            self.game.oro -= 200
            
            # Generar carta aleatoria de rango A
            cofre = Cofre("A")
            carta = cofre.generar_carta()
            
            # Agregar carta al mazo
            self.game.mazo.append(carta)
            
            # Guardar el juego
            from system.Save import guardar_juego
            guardar_juego(self.game)
            
            # Mostrar la carta con Victory y volver a Inventario
            from States.victory import VictoryState
            self.game.change_state(VictoryState(self.game, None, None, carta, titulo="¡Compraste una carta!", volver_a="inventario"))
            
            self.show_menu = False
        else:
            self.mensaje = "No tienes suficiente oro (200 necesarios)"
            self.mensaje_timer = 120
            self.show_menu = False

    def mostrar_info_item(self, item_name):
        """Muestra información del item"""
        self.mensaje = f"Info: {item_name}"
        self.mensaje_timer = 60
        self.show_menu = False

    def usar_item(self, item_name):
        """Usa un item del inventario (poción, etc)"""
        self.mensaje = f"Usaste {item_name}"
        self.mensaje_timer = 60
        self.show_menu = False

    def update(self):
        self.anim_scale += (1 - self.anim_scale) * 0.15
        
        if self.mensaje_timer > 0:
            self.mensaje_timer -= 1

    def draw(self, screen):
        screen.fill((30, 30, 30))
        width = screen.get_width()
        height = screen.get_height()

        draw_text(screen, "Inventario", font_ui, center=True, pos=(width//2, 50))
        
        if not self.show_menu and not self.show_info:
            draw_text(screen, "[ENTER] Ver info    [ESC] Salir", font_ui_mini, center=True, pos=(width//2, 750))
        elif self.show_info:
            draw_text(screen, "[ENTER] Opciones    [ESC] Cerrar    ", font_ui_mini, center=True, pos=(width//2, 750))
        else:
            draw_text(screen, "[ENTER] Confirmar    [ESC] Cancelar", font_ui_mini, center=True, pos=(width//2, 750))

        items = self.get_items()

        start_x = width // 2 - (4 * 200 + 3 * 40) // 2
        start_y = 100

        for i, (item, cantidad) in enumerate(items):

            col = i % 4
            fila = i // 4

            x = start_x + col * (200 + 40)
            y = start_y + fila * (300 + 40)

            seleccionado = (i == self.selected)

            scale = self.anim_scale if seleccionado else 1

            draw_item(
                screen,
                item,
                x,
                y,
                cantidad,
                info=(seleccionado and self.show_info),
                scale=scale
            )
            
            # Resalte de item seleccionado (rectángulo amarillo)
            if seleccionado:
                pygame.draw.rect(screen, (255, 255, 0), (x, y, int(200 * scale), int(300 * scale)), 4)
        
        # Dibujar menú si está abierto
        if self.show_menu:
            self.draw_menu(screen, width, height)
        
        # Dibujar mensaje temporal
        if self.mensaje and self.mensaje_timer > 0:
            draw_text(screen, self.mensaje, font_ui_mini, col=(100, 255, 100), center=True, pos=(width//2, 650))
    
    def draw_menu(self, screen, width, height):
        """Dibuja el menú de opciones"""
        items = self.get_items()
        item_name = items[self.selected][0]
        
        # Fondo oscuro
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Opciones según el item
        if item_name == "Tienda":
            opciones = ["Comprar carta (200 oro)"]
        else:
            opciones = ["Info", "Usar"]
        
        # Dibujar opciones
        menu_height = len(opciones) * 60
        menu_y = height // 2 - menu_height // 2
        
        draw_text(screen, f"Selecciona una acción para {item_name}:", font_ui_mini, center=True, pos=(width//2, menu_y - 60))
        
        for i, opcion in enumerate(opciones):
            y = menu_y + i * 60
            color = (100, 255, 100) if i == self.menu_selected else (255, 255, 255)
            marker = ">>> " if i == self.menu_selected else "    "
            draw_text(screen, marker + opcion, font_ui_mini, col=color, center=True, pos=(width//2, y))