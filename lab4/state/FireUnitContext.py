# fire_unit_state/fire_unit_context.py
from state import FreeState
from state import BusyState

class FireUnitContext:
    def __init__(self, name):
        self.name = name

        # Definicja stanów
        self.free_state = FreeState()
        self.busy_state = BusyState()

        # Początkowy stan to wolny
        self.state = self.free_state

    def set_state(self, state):
        """Zmiana stanu pojazdu."""
        self.state = state

    def dispatch(self):
        """Zadysponowanie pojazdu."""
        self.state.dispatch(self)

    def handle_event(self):
        """Obsługa zdarzenia."""
        self.state.handle_event(self)

    def return_to_base(self):
        """Powrót do bazy."""
        self.state.return_to_base(self)
