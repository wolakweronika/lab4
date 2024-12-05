class Aggregate:
    """Interfejs kolekcji."""
    def iterator(self):
        """Zwraca iterator dla kolekcji."""
        raise NotImplementedError("Method iterator() must be implemented.")
