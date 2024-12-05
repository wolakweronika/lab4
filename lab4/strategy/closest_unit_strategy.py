# closest_unit_strategy.py
from .istrategy import DispatchStrategy
#To tutaj znajduje się logika wyboru najbliższych jednostek.
class ClosestUnitStrategy:
    def dispatch(self, fire_units, location, required_units):
        """Przydziela najbliższe jednostki zgodnie z wymaganiami."""
        # Posortuj jednostki według odległości od zdarzenia
        sorted_units = sorted(fire_units, key=lambda unit: unit.get_distance(location))
        dispatched_units = []  # Lista zadysponowanych jednostek
        total_dispatched = 0  # Liczba całkowicie zadysponowanych pojazdów

        for unit in sorted_units:
            if total_dispatched < required_units:
                # Liczba pojazdów, które można wysłać z tej jednostki
                to_dispatch = min(required_units - total_dispatched, unit.free_units)
                if to_dispatch > 0:
                    unit.mark_units_as_dispatched(to_dispatch)  # Aktualizuj dostępne pojazdy w jednostce
                    dispatched_units.append((unit, to_dispatch))  # Dodaj jednostkę i liczbę pojazdów
                    total_dispatched += to_dispatch  # Zwiększ liczbę zadysponowanych pojazdów

            # Jeśli zadysponowano wystarczającą liczbę pojazdów, zakończ
            if total_dispatched >= required_units:
                break

        return dispatched_units
