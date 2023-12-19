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
        names = ('Роман', 'Валера', 'Акакий', 'Мао')
        name = choice(names)
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
    print('1 - Купить предметы')
    print('2 - Продать предметы')
    print('0 - Выход из лавки')
    option = input('Введите номер опции: ')
    if option == '1':
        for num, item in enumerate(shop_items, 1):
            print(f'{num} - {item}')
        option = input('Введите номер товара чтобы купить или введите 0 для отмены: ')
        # TODO: купить товар по выбранной опции


player = get_hero()
shop_items = ['зелье лечения', 'зелье лечения', 'зелье копчения']
visit_shop(player, shop_items)
