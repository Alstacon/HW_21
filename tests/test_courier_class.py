import pytest

from classes.courier import Courier
from exceptions import ShopIsFull, NotEnoughProduct


class TestCourierClass:

    @pytest.fixture
    def courier_basic(self, request_basic, storages):
        courier = Courier(request_basic, storages)
        return courier

    @pytest.fixture
    def courier_string_quantity(self, request_string_quantity, storages):
        courier = Courier(request_string_quantity, storages)
        return courier

    @pytest.fixture
    def courier_shop_is_full(self, request_shop_is_full, storages):
        courier = Courier(request_shop_is_full, storages)
        return courier

    @pytest.fixture
    def courier_not_enough_prod(self, request_not_enough_prod, storages):
        courier = Courier(request_not_enough_prod, storages)
        return courier

    def test_move_basic(self, courier_basic):
        courier_basic.move()

        assert courier_basic._destination.get_items() == \
               {
                   'помидоры': 2,
                   'огурцы': 2,
                   'земляника': 3,
                   'булки': 4,
                   'морковь': 1
               }

    def test_move_string_quantity(self, courier_string_quantity):
        courier_string_quantity.move()

        assert courier_string_quantity._destination.get_items() == \
               {
                   'картошка': 20,
                   'морковь': 20,
                   'баклажаны': 10,
                   'помидоры': 2
               }

    def test_cancel_add(self, courier_shop_is_full):
        with pytest.raises(ShopIsFull):
            courier_shop_is_full.move()

        courier_shop_is_full.cancel_add()

        assert courier_shop_is_full._sending_point.get_items() == \
               {
                   'картошка': 20,
                   'морковь': 20,
                   'баклажаны': 10
               }

        assert courier_shop_is_full._destination.get_items() == \
               {
                   'помидоры': 2,
                   'огурцы': 2,
                   'земляника': 3,
                   'булки': 4
               }

    def test_cancel_remove(self, courier_not_enough_prod):
        with pytest.raises(NotEnoughProduct):
            courier_not_enough_prod.move()

        courier_not_enough_prod.cancel_remove()

        assert courier_not_enough_prod._sending_point.get_items() == \
               {
                   'картошка': 20,
                   'морковь': 20,
                   'баклажаны': 10
               }

        assert courier_not_enough_prod._destination.get_items() == \
               {
                   'помидоры': 2,
                   'огурцы': 2,
                   'земляника': 3,
                   'булки': 4
               }
