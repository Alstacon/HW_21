import pytest

from classes.request_class import Request
from exceptions import InvalidRequest


class TestRequestClass:
    requests_wrong_point = ["Доставить всю морковь со склада в никуда",
                            "Доставить всю морковь с Марса в магазин",
                            "Доставить всю морковь с Марса в никуда"]

    def test_basic_request(self, storages):
        request = Request("Доставить 1 морковь со склада в магазин", storages)
        assert request.quantity == 1
        assert request.sending_point == 'склад'
        assert request.destination == 'магазин'
        assert request.product == 'морковь'

        request = Request("Доставить 1 морковочку со склада в магазин", storages)
        assert request.quantity == 1
        assert request.sending_point == 'склад'
        assert request.destination == 'магазин'
        assert request.product == 'морковочку'
        assert request.product_for_search == 'морковь'

        request = Request("Доставить всю морковочку из магазина на склад", storages)
        assert request.quantity == 'всю'
        assert request.sending_point == 'магазин'
        assert request.destination == 'склад'
        assert request.product == 'морковочку'
        assert request.product_for_search == 'морковь'


    def test_wrong_request(self, storages):
        with pytest.raises(InvalidRequest):
            Request("1 морковь со склада в магазин", storages)

    def test_request_string_quantity(self, storages):
        request = Request("Доставить всю морковь со склада в магазин", storages)
        assert request.quantity == 'всю'

    @pytest.mark.parametrize('requests_wrong_point', requests_wrong_point)
    def test_requests_wrong_points(self, requests_wrong_point, storages):
        with pytest.raises(InvalidRequest):
            Request(requests_wrong_point[0], storages)
            Request(requests_wrong_point[1], storages)
            Request(requests_wrong_point[2], storages)
