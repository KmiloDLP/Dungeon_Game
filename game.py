from states.menu import MenuState
from states.combate import CombatState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = MenuState(self)

        self.mazo = []
        self.inventario = []
        self.oro = 0

    def change_state(self, new_state):
        self.state = new_state

    def handle_event(self, event):
        self.state.handle_event(event)

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw(self.screen)