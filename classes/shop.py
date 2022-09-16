from exceptions import ShopIsFull, ProductNotFound, NotEnoughProduct
from classes.store import Store


class Shop(Store):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name, quantity) -> None:
        if len([key for key in self._items.keys()]) == 5 or self.get_free_space() < quantity:
            raise ShopIsFull

        else:
            if not self._items.get(name):
                self._items[name] = quantity
            else:
                self._items[name] += quantity

    def remove(self, name: str, quantity: int) -> None:
        if not self._items.get(name):
            raise ProductNotFound

        if quantity <= self._items[name]:
            self._items[name] -= quantity
            if self._items[name] == 0:
                self._items.pop(name)

        else:
            raise NotEnoughProduct

