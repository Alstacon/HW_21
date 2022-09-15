import pytest as pytest

from classes.store_class import Store
from exceptions import StoreIsFull, ProductNotFound, NotEnoughProduct


class TestStoreClass:


    def test_add(self, store):
        store.add('яблоки', 5)
        store.add('вишня', 1)

        assert store.get_items() == {'картошка': 20,
                                     'морковь': 20,
                                     'баклажаны': 10,
                                     'яблоки': 5,
                                     'вишня': 1}

        store.add('яблоки', 5)
        assert store.get_items() == {'картошка': 20,
                                     'морковь': 20,
                                     'баклажаны': 10,
                                     'яблоки': 10,
                                     'вишня': 1}

    def test_add_store_is_full(self, store):
        with pytest.raises(StoreIsFull):
            store.add('селедка', 100)

    def test_add_incorrect_arguments(self, store):
        with pytest.raises(TypeError):
            store.add()

        with pytest.raises(AssertionError):
            assert store.add(3, 3)
            assert store.add("еда", "много")

    def test_remove(self, store):
        store.remove('картошка', 20)
        store.remove('морковь', 1)

        assert store.get_items() == {'морковь': 19,
                                     'баклажаны': 10, }

    def test_remove_prod_not_found(self, store):
        with pytest.raises(ProductNotFound):
            store.remove('вишня', 20)

    def test_remove_not_enough_prod(self, store):
        with pytest.raises(NotEnoughProduct):
            store.remove('картошка', 200)

    def test_get_free_space(self, store):
        assert store.get_free_space() == 50

        store.add('яблоки', 5)
        assert store.get_free_space() == 45

    def test_get_unique_items(self, store):
        assert store.get_unique_items_count() == 3

        store.add('яблоки', 5)
        assert store.get_unique_items_count() == 4



