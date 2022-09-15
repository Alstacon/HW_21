class BaseError(Exception):
    message = "Неизвестная ошибка"

class StoreIsFull(BaseError):
    message = "Склад переполнен. Доставка невозможна"

class NotEnoughProduct(BaseError):
    message = "Недостаточно товаров"

class ProductNotFound(BaseError):
    message = "Такого товара нет"

class ShopIsFull(BaseError):
    message = "Магазин переполнен. Доставка невозможна"

class InvalidRequest(BaseError):
    message = "Некорректный запрос"





