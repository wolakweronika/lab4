class Iterator:
    """Interfejs iteratora."""
    def has_next(self):
        """Sprawdza, czy są kolejne elementy."""
        raise NotImplementedError("Method has_next() must be implemented.")

    def next(self):
        """Zwraca kolejny element."""
        raise NotImplementedError("Method next() must be implemented.")
