import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random


class Visualizer:
    def __init__(self, units, width=800, height=600):
        self.units = units
        self.width = width
        self.height = height
        self.running = True  # Ustawienie atrybutu running na True

        # Map bounds for translating coordinates
        self.map_bounds = {
            "lat_min": 49.95855025648944,
            "lat_max": 50.154564013341734,
            "lon_min": 19.688292482742394,
            "lon_max": 20.02470275868903,
        }

        # Create figure and axis
        self.fig, self.ax = plt.subplots(figsize=(width / 100, height / 100))
        self.ax.set_xlim(self.map_bounds["lon_min"], self.map_bounds["lon_max"])
        self.ax.set_ylim(self.map_bounds["lat_min"], self.map_bounds["lat_max"])
        self.ax.set_title("Kraków - Dyspozycja jednostek PSP")
        self.ax.set_xlabel("Longitude")
        self.ax.set_ylabel("Latitude")

    def _transform_coordinates(self, lat, lon):
        """Transform WGS-84 coordinates to map coordinates."""
        return lon, lat

    def draw_units(self):
        """Draw all fire units on the map."""
        for unit in self.units:
            x, y = self._transform_coordinates(unit.location[0], unit.location[1])
            color = "green" if unit.free_units > 0 else "red"
            self.ax.add_patch(patches.Circle((x, y), 0.005, color=color, label=f"JRG {unit.name}"))

    def draw_event(self, event):
        """Draw the event on the map."""
        x, y = self._transform_coordinates(event["location"][0], event["location"][1])
        self.ax.add_patch(patches.Circle((x, y), 0.005, color="yellow"))

    def update_screen(self, event=None):
        """Update the screen."""
        self.ax.clear()
        self.ax.set_xlim(self.map_bounds["lon_min"], self.map_bounds["lon_max"])
        self.ax.set_ylim(self.map_bounds["lat_min"], self.map_bounds["lat_max"])
        self.ax.set_title("Kraków - Dyspozycja jednostek PSP")
        self.ax.set_xlabel("Longitude")
        self.ax.set_ylabel("Latitude")

        # Draw all units
        self.draw_units()

        # Draw the event
        if event:
            self.draw_event(event)

        # Show the updated map
        plt.pause(0.5)

    def handle_events(self):
        """Handle quitting."""
        plt.show(block=True)
