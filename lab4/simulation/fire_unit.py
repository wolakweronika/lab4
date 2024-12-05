from state.BusyState import BusyState
from state.FreeState import FreeState
import random
import time
class FireUnit:
    def __init__(self, name, location, total_units=5):
        self.name = name
        self.location = location
        self.total_units = total_units
        self.free_units = total_units  # Początkowo wszystkie jednostki są wolne

        # Stany
        self.free_state = FreeState()
        self.busy_state = BusyState()
        self.state = self.free_state  # Początkowy stan to wolny
    
    def set_state(self, state):
        """Zmienia bieżący stan jednostki."""
        self.state = state

    def dispatch(self):
        """Zadysponowanie pojazdu."""
        self.state.dispatch(self)

    def handle_event(self, location):
        """Obsługa zdarzenia w danej lokalizacji."""
        if self.state != self.busy_state:
            print(f"{self.name} cannot handle event because it is not in busy state.")
            return

        # Symulacja czasu dojazdu na miejsce zdarzenia (0-3 sekundy)
        travel_time = random.randint(0, 3)
        print(f"{self.name} is traveling to the event location... Estimated time: {travel_time}s")
        time.sleep(travel_time)

        # Losowa decyzja: czy zdarzenie jest fałszywym alarmem (5% szans)
        is_false_alarm = random.random() < 0.05

        if is_false_alarm:
            print(f"{self.name} encountered a false alarm. Returning to base.")
        else:
            # Symulacja działań na miejscu zdarzenia (5-25 sekund)
            action_time = random.randint(5, 25)
            print(f"{self.name} is handling the event... Estimated time: {action_time}s")
            time.sleep(action_time)
            print(f"{self.name} has finished handling the event.")

        # Powrót do bazy
        self.return_to_base()


    def return_to_base(self):
        
        """Powrót do bazy po zakończeniu akcji."""
        return_time = random.randint(0, 3)
        print(f"{self.name} is returning to base... Estimated time: {return_time}s")
        time.sleep(return_time)
        print(f"{self.name} has returned to base.")
        self.mark_units_as_free(1)  # Zwiększ liczbę wolnych jednostek

    def update(self, event):
        """
        Reaguje na powiadomienie od SKKM.
        Event zawiera typ zdarzenia i lokalizację.
        """
        event_type, location = event["type"], event["location"]
        print(f"{self.name} received event: {event_type} at {location}")

        if self.free_units > 0:
            print(f"{self.name} has {self.free_units} free units and can respond.")
        else:
            print(f"{self.name} is busy and cannot respond to this event.")

    def get_available_units(self):
        """Zwraca liczbę dostępnych jednostek."""
        return [self] * self.free_units if self.state == self.free_state else []

    def mark_units_as_dispatched(self, count):
        """Zmniejsza liczbę dostępnych pojazdów, z walidacją."""
        if count > self.free_units:
            raise ValueError(f"Cannot dispatch {count} units; only {self.free_units} available.")
        self.free_units -= count
        print(f"{self.name} dispatched {count} units. {self.free_units} remaining.")
        if self.free_units == 0:
            self.set_state(self.busy_state)

    def mark_units_as_free(self, count):
        """Zwiększa liczbę dostępnych pojazdów, z walidacją."""
        if self.free_units + count > self.total_units:
            raise ValueError(f"Cannot free {count} units; total units would exceed {self.total_units}.")
        self.free_units += count
        print(f"{self.name} returned {count} units. {self.free_units} now available.")

    def get_distance(self, location):
        """Oblicza odległość od zdarzenia."""
        return ((self.location[0] - location[0]) ** 2 + (self.location[1] - location[1]) ** 2) ** 0.5
