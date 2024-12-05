class Observer:
    """Interface for observers."""
    def update(self, event_type, location):
        raise NotImplementedError("The 'update' method must be implemented by subclasses.")

class ObservedSubject:
    """Class representing the subject being observed."""
    def __init__(self):
        self.observers = []  # List of observers

    def add_observer(self, observer):
        """Adds an observer to the list."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Removes an observer from the list."""
        self.observers.remove(observer)

    def notify_observers(self, event_type, location):
        """Notifies all observers of an event."""
        for observer in self.observers:
            observer.update(event_type, location)

# ---- State Pattern ----