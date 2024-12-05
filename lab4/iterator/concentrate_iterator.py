from .iterator import Iterator

class ConcreteIterator(Iterator):
    """Konkretna implementacja iteratora."""
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        """Sprawdza, czy są kolejne elementy w kolekcji."""
        return self._index < len(self._collection)

    def next(self):
        """Zwraca kolejny element w kolekcji."""
        if not self.has_next():
            raise StopIteration("No more elements in the collection.")
        item = self._collection[self._index]
        self._index += 1
        return item
