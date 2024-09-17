class Store:
    def __init__(self, name: str, address: str, items: dict):
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, item: str, price: float):
        self.items[item] = price

    def del_item(self, item: str):
        try:
            return self.items.pop(item)
        except KeyError:
            return 'Товар не найден'

    def get_price(self, item: str):
        if self.items[item]:
            return self.items[item]
        else:
            return None

    def update_price(self, item: str, price: float):
        if self.items[item]:
            self.items[item] = price
        else:
            print('Товар не найден')

    def store_info(self):
        print(f'Название магазина: {self.name}')
        print(f'Адрес магазина: {self.address}')
        print(f'Номенклатура магазина: {self.items}')
        print()


store_1 = Store('"Рога и копыта"', "Рогокопытная 1, 48", {'Рога': 10, 'Копыта': 20})
store_2 = Store('"Копыта и рога"', "Копыторожская 48, 1", {'Рога': 30, 'Копыта': 40})
store_3 = Store('"Рога без копыт"', "Безкопытная 1, 1", {'Рога': 50, 'Рожки': 60})

print('2) Вывести данные магазинов')
store_1.store_info()
store_2.store_info()
store_3.store_info()

print()
print(f'3) Проверить методы на магазине {store_1.name}')

store_1.add_item('Уши', 30)
store_1.add_item('Хвосты', 40)
print(f'3.1) Добавлены новые товары, текущая номенклатура {store_1.items}')

store_1.del_item('Уши')
print(f'3.2) Удален товар "Уши", текущая номенклатура: {store_1.items}')
print(f'3.3) При повторном удалении, товар не найден, пользователь получает сообщение: {store_1.del_item('Уши')}')

store_1.update_price('Хвосты', 10.5)
print(f'3.4) Изменена стоимость товара "Хвосты", текущая цена: {store_1.items["Хвосты"]}')
