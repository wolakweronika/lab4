import random

class EventGenerator:
    def __init__(self, bounds, probabilities):
        self.bounds = bounds
        self.probabilities = probabilities

    def generate_event(self):
        lat = random.uniform(self.bounds[0][0], self.bounds[1][0])
        lon = random.uniform(self.bounds[0][1], self.bounds[1][1])
        event_type = random.choices(["PZ", "MZ"], weights=self.probabilities, k=1)[0]
        return {"type": event_type, "location": (lat, lon)}
