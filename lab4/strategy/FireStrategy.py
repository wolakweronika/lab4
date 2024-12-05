# strategy/fire_event_strategy.py
from strategy.istrategy import DispatchStrategy
from strategy.closest_unit_strategy import ClosestUnitStrategy

class FireEventStrategy:
    def dispatch(self, fire_units, location, required_units):
        """Przydziela jednostki do pożaru."""
        return ClosestUnitStrategy().dispatch(fire_units, location, required_units)