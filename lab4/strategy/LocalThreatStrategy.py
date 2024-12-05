# strategy/local_threat_strategy.py
from strategy.istrategy import DispatchStrategy

from strategy.closest_unit_strategy import ClosestUnitStrategy

class LocalThreatStrategy:
    def dispatch(self, fire_units, location, required_units):
        """Przydziela jednostki do miejscowego zagrożenia."""
        return ClosestUnitStrategy().dispatch(fire_units, location, required_units)