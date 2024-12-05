# fire_unit_state/free_state.py
from state._init_ import State

class FreeState(State):
    def dispatch(self, fire_unit):
        print(f"{fire_unit.name} is dispatched to an event.")
        fire_unit.set_state(fire_unit.busy_state)  # Zmiana stanu na zajęty

    def handle_event(self, fire_unit):
        print(f"{fire_unit.name} is free and cannot handle an event.")

    def return_to_base(self, fire_unit):
        print(f"{fire_unit.name} is already at base and free.")
