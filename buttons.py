from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

#кнопки после старта
def after_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = types.KeyboardButton('Menu')
    log_out = types.KeyboardButton('Log out')
    markup.add(menu, log_out)
    return markup

def menu_menu():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    coffee = types.KeyboardButton('Coffee')
    sweets = types.KeyboardButton('Sweets')
    snacks = types.KeyboardButton('Snacks')
    other = types.KeyboardButton('Other')
    back = types.KeyboardButton('Back')
    buttons.add(coffee, sweets, snacks, other, back)
    return buttons

def coffee():
    coffee = types.ReplyKeyboardMarkup(resize_keyboard=True)
    americano = types.KeyboardButton('Americano')
    latte = types.KeyboardButton('Latte')
    cappucino = types.KeyboardButton('Capuccino')
    espresso = types.KeyboardButton('Espresso')
    back = types.KeyboardButton('Back')
    coffee.add(americano, latte, cappucino, espresso, back)
    return coffee

def sweets1():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    cheesecake = KeyboardButton('Cheesecake')
    ecklers = KeyboardButton('Ecklers')
    donuts = KeyboardButton('Donuts')
    cakes = KeyboardButton('Cakes')
    back = KeyboardButton('Back')
    buttons.add( cheesecake, ecklers, donuts, cakes, back)
    return buttons

def snacks():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    sandwich = KeyboardButton('Sandwich')
    omelette = KeyboardButton('Omelette')
    burger_french_rice = KeyboardButton('Burger with french fries')
    back = KeyboardButton('Back')
    buttons.add(sandwich, omelette, burger_french_rice, back)
    return buttons

def image_buttons(plus_or_minus='', current_amount=1):
    buttons = InlineKeyboardMarkup(row_width=3)
    back = InlineKeyboardButton(text='Назад', callback_data='back')
    plus = InlineKeyboardButton(text='+', callback_data='plus')
    minus = InlineKeyboardButton(text='-', callback_data='minus')
    count = InlineKeyboardButton(text=str(current_amount), callback_data=str(current_amount))
    cart = InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')

    # Отслеживать плюс или минус
    if plus_or_minus == 'plus':
        new_amount = int(current_amount) + 1

        count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    elif plus_or_minus == 'minus':
        if int(current_amount) > 1:
            new_amount = int(current_amount) - 1

            count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    # Обединить кнопки с пространством
    buttons.add(minus, count, plus)
    buttons.row(cart)
    buttons.row(back)

    return buttons

def get_accept():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)

    yes = KeyboardButton('Подтвердить')
    no = KeyboardButton('Отменить')

    buttons.add(yes, no)

    return buttons

def get_cart():
    buttons = InlineKeyboardMarkup(row_width=1)

    clear_cart = InlineKeyboardButton(text='Очистить корзину', callback_data='clear_cart')
    order = InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    back = InlineKeyboardButton(text='Назад', callback_data='back')

    buttons.add(clear_cart, order, back)

    return buttons

def number_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num_button = types.KeyboardButton('Поделиться контактом', request_contact=True)

    buttons.add(num_button)

    return buttons


def geo_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    g_button = types.KeyboardButton('Поделиться локацием', request_location=True)

    buttons.add(g_button)

    return buttons