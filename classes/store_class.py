from exceptions import StoreIsFull, ProductNotFound, NotEnoughProduct
from classes.storage_abs_class import Storage


class Store(Storage):
    def __init__(self, items: dict[str, int], capacity: int = 100):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, name: str, quantity: int):
        if self.get_free_space() < quantity:
            raise StoreIsFull

        if quantity <= self.get_free_space():
            if not self._items.get(name):
                self._items[name] = quantity
            else:
                self._items[name] += quantity

    def remove(self, name, quantity):
        self._items.get(name, ProductNotFound)

        if quantity <= self._items[name]:
            self._items[name] -= quantity
            if self._items[name] == 0:
                self._items.pop(name)

        else:
            raise NotEnoughProduct

    def get_free_space(self):
        return self.capacity - sum([value for value in self._items.values()])

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items.keys())
