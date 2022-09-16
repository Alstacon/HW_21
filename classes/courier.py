from classes.request import Request
from exceptions import ProductNotFound


class Courier:

    def __init__(self, request: Request, storages: dict):
        self._request = request
        if self._request.sending_point in storages:
            self._sending_point = storages[self._request.sending_point]
        if self._request.destination in storages:
            self._destination = storages[self._request.destination]

        if self._request.quantity in ['все', 'всю', 'весь', 'всё']:
            if self._request.product_for_search not in self._sending_point.get_items().keys():
                raise ProductNotFound
            else:
                self.quantity = self._sending_point.get_items()[self._request.product_for_search]
        else:
            self.quantity = self._request.quantity

    def move(self) -> None:
        self._sending_point.remove(name=self._request.product_for_search, quantity=self.quantity)
        print(f"Курьер забрал {self.quantity} {self._request.product} из {self._request.sending_point}а \
и везет в {self._request.destination}.\nВ {self._request.sending_point}е хранится: {self._sending_point.get_items()}\n")

        self._destination.add(name=self._request.product_for_search, quantity=self.quantity)
        print(f"Курьер доставил {self.quantity} {self._request.product} в {self._request.destination}.\n"
              f"В {self._request.destination}е хранится: {self._destination.get_items()}")

    def cancel_remove(self) -> None:
        self._sending_point.add(name=self._request.product_for_search, quantity=0)

    def cancel_add(self) -> None:
        self._sending_point.add(name=self._request.product_for_search, quantity=self.quantity)
