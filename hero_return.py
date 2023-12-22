from random import choice


def get_hero(
        name=None,
        hp=100,
        level=1,
        xp=0,
        money=25,
        inventory=None
        ) -> list:
    ''' Возвращает список - героя с 6 характеристиками '''
    if not name:
        name = choice(['Роман', 'Валера', 'Акакий', 'Мао'])
    if not inventory:
        inventory = []
    return [name, hp, level, xp, money, inventory]


def show_hero(hero: list) -> None:
    ''' Выводит на экран все 6 характеристик героя '''
    print('имя:', hero[0])
    print('здоровье:', hero[1])
    print('уровень:', hero[2])
    print('опыт:', hero[3])
    print('деньги:', hero[4])
    print('инвентарь:', *hero[5])
    print('-' * 10)


def visit_shop(hero: list, shop_items: list):
    '''
    Показывает характеристики героя
    Выводит на экран текст магазина
    Выводит на экран опции пронумерованные опции
    Предлагает герою выбор опции
    Работает по выбранной опции
    '''
    show_hero(hero)
    print(f'{hero[0]}, приехал в лавку')
    print('Временная распродажа: все товары по 10 монет!')
    price_tmp = 10
    print('1 - Купить предметы')
    print('2 - Продать предметы')
    print('0 - Выход из лавки')
    option = input('Введите номер опции: ')
    if option == '1':
        for num, item in enumerate(shop_items, 1):
            print(f'{num} - {item}')
        print('0 - Отмена')
        option = input('Введите номер опции чтобы купить или 0 для отмены: ')
        if int(option) < 0 or int(option) > len(shop_items):
            print('Неверная опция')
        elif option == '0':
            print('Выходим из покупок')
        else:
            item_index = int(option) - 1
            item_name = shop_items[item_index]
            #print(f'{hero[0]} купил {item_name}')
            if hero[4] < price_tmp:
                print(f'У {hero[0]} недостаточно денег')
            else:
                hero[4] -= price_tmp
                hero[5].append(item_name)
                shop_items.pop(item_index)
                print(f'{hero[0]} купил {item_name}')


player = get_hero()
shop_items = ['зелье лечения', 'зелье лечения', 'зелье копчения']
visit_shop(player, shop_items)
show_hero(player)
print(shop_items)
