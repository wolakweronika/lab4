# fire_unit_state/busy_state.py
import random
import time
from state._init_ import State

class BusyState(State):
    def dispatch(self, fire_unit):
        print(f"{fire_unit.name} is currently busy and cannot be dispatched.")

    def handle_event(self, fire_unit, location):
        travel_time = random.randint(0, 3)
        print(f"{fire_unit.name} is traveling to the event location... Estimated time: {travel_time}s")

        is_false_alarm = random.random() < 0.05
        if is_false_alarm:
            print(f"{fire_unit.name} encountered a false alarm. Returning to base.")
        else:
            action_time = random.randint(5, 25)
            print(f"{fire_unit.name} is handling the event... Estimated time: {action_time}s")
            print(f"{fire_unit.name} has finished handling the event.")

        self.return_to_base(fire_unit)

    def return_to_base(self, fire_unit):
        return_time = random.randint(0, 3)
        print(f"{fire_unit.name} is returning to base... Estimated time: {return_time}s")
        
        fire_unit.set_state(fire_unit.free_state)