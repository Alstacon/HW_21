import pytest as pytest

from classes.shop_class import Shop
from exceptions import ShopIsFull, ProductNotFound, NotEnoughProduct


class TestShopClass:


    def test_add(self, shop):
        shop.add('яблоки', 9)

        assert shop.get_items() == {'помидоры': 2,
                                    'огурцы': 2,
                                    'земляника': 3,
                                    'булки': 4,
                                    'яблоки': 9,
                                    }

    def test_add_shop_is_full(self, shop):
        with pytest.raises(ShopIsFull):
            shop.add('селедка', 10)

        with pytest.raises(ShopIsFull):
            shop.add('селедка', 1)
            shop.add('земляника', 1)

    def test_add_incorrect_arguments(self, shop):
        with pytest.raises(TypeError):
            shop.add()

        with pytest.raises(AssertionError):
            assert shop.add(3, 3)
            assert shop.add("еда", "много")

    def test_remove(self, shop):
        shop.remove('булки', 1)
        shop.remove('земляника', 1)

        assert shop.get_items() == {
                                    'помидоры': 2,
                                    'огурцы': 2,
                                    'земляника': 2,
                                    'булки': 3
                                }

    def test_remove_prod_not_found(self, shop):
        with pytest.raises(ProductNotFound):
            shop.remove('вишня', 20)

    def test_remove_not_enough_prod(self, shop):
        with pytest.raises(NotEnoughProduct):
            shop.remove('булки', 200)

    def test_get_free_space(self, shop):
        assert shop.get_free_space() == 9

        shop.add('яблоки', 5)
        assert shop.get_free_space() == 4

    def test_get_unique_items(self, shop):
        assert shop.get_unique_items_count() == 4

        shop.add('яблоки', 5)
        assert shop.get_unique_items_count() == 5
