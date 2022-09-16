from exceptions import InvalidRequest
from classes.products import Products


class Request:

    def __init__(self, request: str, storages: dict):

        splitted_request = request.lower().split(' ')

        if len(splitted_request) != 7:
            raise InvalidRequest

        self.quantity = splitted_request[1]
        if self.quantity not in ['все', 'всю', 'весь']:
            self.quantity = int(self.quantity)
        else:
            self.quantity = splitted_request[1]
        self.product, self.product_for_search = Products(splitted_request[2]).declension()
        self.sending_point = splitted_request[4].rstrip('а')
        self.destination = splitted_request[6]

        if self.sending_point not in storages or self.destination not in storages:
            raise InvalidRequest

