import random
import time
from simulation.observer import ObservedSubject
from simulation.event_generator import EventGenerator
from strategy.closest_unit_strategy import ClosestUnitStrategy
from iterator.aggregate import Aggregate
from iterator.concentrate_iterator import ConcreteIterator
from strategy.FireStrategy import FireEventStrategy
from strategy.LocalThreatStrategy import LocalThreatStrategy


class SKKM(Aggregate, ObservedSubject):
    def __init__(self, event_generator):
        super().__init__()
        self.observers = []  # Lista jednostek strażackich
        self.event_generator = event_generator  # Generator zdarzeń
        self.fire_strategy = FireEventStrategy()  # Strategia dla zdarzeń pożarów
        self.local_threat_strategy = LocalThreatStrategy()  # Strategia dla miejscowych zagrożeń
    
    def add_observer(self, observer):
        """Dodaje jednostkę strażacką jako obserwatora."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Usuwa jednostkę strażacką jako obserwatora."""
        self.observers.remove(observer)

    def notify_observers(self, event):
        """Powiadamia wszystkich obserwatorów o nowym zdarzeniu."""
        for observer in self.observers:
            observer.update(event)

    def iterator(self):
        """Zwraca iterator do przeglądania jednostek strażackich."""
        return ConcreteIterator(self.observers)

    def handle_multiple_events(self, events):
        """
        Obsługuje wiele zdarzeń jednocześnie, pozwalając na równoczesne przetwarzanie.
        """
        print("\nSKKM is handling multiple events:")
        for event in events:
            print(f"Event: {event['type']} at {event['location']}")

            # Wybierz odpowiednią strategię na podstawie typu zdarzenia
            if event["type"] == "PZ":  # Pożar
                strategy = self.fire_strategy
                required_units = 3
            elif event["type"] == "MZ":  # Miejscowe zagrożenie
                strategy = self.local_threat_strategy
                required_units = 2
            else:
                print(f"Unknown event type: {event['type']}")
                continue

            # Przydziel jednostki zgodnie ze strategią
            dispatched = strategy.dispatch(self.observers, event["location"], required_units)
            if dispatched:
                for unit, count in dispatched:
                    print(f"Dispatched {count} unit(s) from {unit.name} for event at {event['location']}.")
                    self._start_event(unit, count, event["location"])
            else:
                print(f"No available units to dispatch for event at {event['location']}!")
    
    def _start_event(self, unit, count, location):
        """
        Rozpoczyna obsługę zdarzenia dla jednostki bez oczekiwania na zakończenie innych zdarzeń.
        """
        for _ in range(count):
            # Każdy pojazd przetwarza zdarzenie niezależnie
            unit.set_state(unit.busy_state)
            unit.state.handle_event(unit, location)