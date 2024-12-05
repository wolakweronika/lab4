# dispatcher.py
#w większym systemie, gdzie strategia może być często zmieniana lub zarządzana dynamicznie,
# Dispatcher służy jako centralny punkt dla zarządzania strategią.
from .istrategy import DispatchStrategy

class Dispatcher:
    def __init__(self, strategy: DispatchStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DispatchStrategy):
        self.strategy = strategy

    def dispatch_units(self, fire_units, location, required_units):
        return self.strategy.dispatch(fire_units, location, required_units)
