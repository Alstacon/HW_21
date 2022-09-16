import pytest

from classes.request import Request
from classes.shop import Shop
from classes.store import Store


@pytest.fixture
def shop():
    shop = Shop({
        'помидоры': 2,
        'огурцы': 2,
        'земляника': 3,
        'булки': 4
    })
    return shop


@pytest.fixture
def store():
    store = Store({
        'картошка': 20,
        'морковь': 20,
        'баклажаны': 10
    })
    return store


@pytest.fixture
def storages(store, shop):
    storages = {
        'склад': store,
        'складе': store,
        'склада': store,
        'магазин': shop,
        'магазине': shop,
        'магазина': shop
    }
    return storages


@pytest.fixture
def request_basic(storages):
    request = Request(
        "Доставить 1 морковь из склада в магазин",
        storages
    )
    return request


@pytest.fixture
def request_string_quantity(storages):
    request = Request(
        "Доставить все помидорки из магазина на склад",
        storages
    )
    return request

@pytest.fixture
def request_shop_is_full(storages):
    request = Request(
        "Доставить всю картошку со склада в магазин",
        storages
    )
    return request\


@pytest.fixture
def request_not_enough_prod(storages):
    request = Request(
        "Доставить 100 картошек со склада в магазин",
        storages
    )
    return request


