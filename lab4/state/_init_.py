# fire_unit_state/__init__.py
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def dispatch(self, fire_unit):
        """Próba zadysponowania pojazdu."""
        pass

    @abstractmethod
    def handle_event(self, fire_unit):
        """Obsługa zdarzenia na miejscu."""
        pass

    @abstractmethod
    def return_to_base(self, fire_unit):
        """Powrót do bazy i zmiana stanu na wolny."""
        pass
