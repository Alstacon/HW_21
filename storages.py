from classes.shop import Shop
from classes.store import Store


store = Store({
    'картошка': 10,
    'морковь': 15,
    'баклажаны': 8
})

shop = Shop({
    'помидоры': 7,
    'огурцы': 2,
})

storages = {
    'склад': store,
    'складе': store,
    'склада': store,
    'магазин': shop,
    'магазине': shop,
    'магазина': shop
}
