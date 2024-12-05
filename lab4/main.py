import sys
import os
import time
import random

# Dodanie folderu "simulation" do ścieżki
sys.path.append(os.path.join(os.path.dirname(__file__), "simulation"))

# Importowanie modułów
from strategy.closest_unit_strategy import ClosestUnitStrategy
from strategy.dispatcher import Dispatcher
from strategy.istrategy import DispatchStrategy

from simulation.SKKM import SKKM
from iterator.iterator import Iterator
from simulation.event_generator import EventGenerator
from simulation.fire_unit import FireUnit
from simulation.visualizer import Visualizer


if __name__ == "__main__":
    # Definicja granic i prawdopodobieństw dla zdarzeń
    bounds = ((49.95855025648944, 19.688292482742394), (50.154564013341734, 20.02470275868903))
    probabilities = [30, 70]  # Prawdopodobieństwo: 30% PZ, 70% MZ
    
    fixed_location = (50.070, 19.940) 
    event_types = ["PZ", "MZ"]  # Definiowanie event_types
     # Stała lokalizacja (np. Kraków)
    # Inicjalizacja generatora zdarzeń
    event_generator = EventGenerator(bounds, probabilities)

    
    # Inicjalizacja SKKM z generatora zdarzeń
    skkm = SKKM(event_generator)

    # Tworzenie jednostek strażackich
    # Tworzenie jednostek strażackich z predefiniowanymi danymi geograficznymi
    fire_units = [
        FireUnit("JRG-1", (50.05999546754905, 19.94311273940794)),
        FireUnit("JRG-2", (50.0334788502075, 19.9359033914334)),
        FireUnit("JRG-3", (50.075782424336374, 19.887523751004867)),
        FireUnit("JRG-4", (50.037798842647675, 20.00614171409626)),
        FireUnit("JRG-5", (50.09173580126222, 19.920381753047778)),
        FireUnit("JRG-6", (50.016213431628586, 20.01607871649386)),
        FireUnit("JRG-7", (50.09408065317086, 19.977735182621227)),
        FireUnit("JRG Szkoły Aspirantów PSP", (50.077461950994866, 20.033159628860805)),
        FireUnit("JRG Skawina", (49.968484671124315, 19.799516377610022)),
        FireUnit("LSP Lotniska w Balicach", (50.07365368416614, 19.785828235745207)),
    ]


    # Rejestracja jednostek jako obserwatorów
    for unit in fire_units:
        skkm.add_observer(unit)

    print("Iterating through fire units:")
    iterator = skkm.iterator()
    while iterator.has_next():
        unit = iterator.next()
        print(f"Fire Unit: {unit.name}")

    # Obsługa wielu zdarzeń
    concurrent_events = [
        {"type": "PZ", "location": fixed_location},
        {"type": "MZ", "location": fixed_location},
        {"type": "PZ", "location": fixed_location},
    ]

    # Obsługa równoczesnych zdarzeń
    print("\n--- Handling Concurrent Events ---")
    skkm.handle_multiple_events(concurrent_events)
    time.sleep(20)

    skkm.handle_multiple_events(concurrent_events)

    skkm.handle_multiple_events(concurrent_events)