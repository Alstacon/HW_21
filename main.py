from classes.courier import Courier
from exceptions import ShopIsFull, BaseError, NotEnoughProduct
from classes.request import Request
from storages import storages


def main():
    while True:

        print("\nДобрый день!\n")

        for storage_name in ['на складе', 'в магазине']:
            print(f"""Сейчас {storage_name}:\n {storages[storage_name.split(' ')[-1]].get_items()}""")

        user_input = input(
            """\nВведите запрос типа 'Доставить 3 печеньки из склада в магазин'\nВведите "стоп", когда закончите""")

        if user_input == "стоп" or user_input == "stop":
            break

        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        try:
            courier = Courier(request, storages)
        except BaseError as error:
            print(error.message)
            continue

        try:
            courier.move()
        except NotEnoughProduct as error:
            courier.cancel_remove()
            print(error.message)
        except ShopIsFull as error:
            courier.cancel_add()
            print(error.message)
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
