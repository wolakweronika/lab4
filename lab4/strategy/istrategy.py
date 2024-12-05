# Cel: Ustalenie wspólnego interfejsu (tu metody dispatch) dla wszystkich strategii dyspozycji jednostek straży pożarnej.
#Każda konkretna strategia implementuje tę metodę na swój sposób
class DispatchStrategy:
    def dispatch(self, fire_units, location, required_units):
        raise NotImplementedError("Dispatch strategy must implement 'dispatch' method.")
