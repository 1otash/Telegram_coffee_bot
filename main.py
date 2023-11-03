# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import telebot
import buttons
import database
bot = telebot.TeleBot('6515369934:AAFoguOT6hs9AFDY0kfsJeQJzW8Ogcc48uo')
users = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    checker = database.check_user(user_id)
    # Если пользователь есть в базе
    if checker:
        # Получаем актуальный список продуктов
        products = database.get_pr_name_id()

        # Отправим сообщение с меню
        bot.send_message(user_id, 'Привет')
        bot.send_message(user_id, 'Choose your options', reply_markup=buttons.after_start())
        bot.register_next_step_handler(message, menu)

    # Если пользователя нету в базе
    elif not checker:
        bot.send_message(user_id, 'Привет отправьте свое имя')

        # Переход на этап получения имени
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id = message.from_user.id

    # сохранить имю в переменную
    username = message.text

    # Отправим ответ
    bot.send_message(user_id, 'Отправьте номер телефона', reply_markup=buttons.number_buttons())
    bot.register_next_step_handler(message, get_number, username)

# def get_location(message, username):
#     user_id = message.from_user.id
#     if message.location:
#         user_location = message.location
#         bot.send_message(user_id, 'Отправьте номер телефона', reply_markup=buttons.number_buttons())
#         bot.register_next_step_handler(message, get_number, username, user_location)
#     else:
#         bot.send_message(user_id, 'Отправьте локацию через кнопку!')
#         bot.register_next_step_handler(message, get_location, username)


# получаем номер пользователя
def get_number(message, name):
    user_id = message.from_user.id

    if message.contact:
        # сохраняем контакт
        phone_number = message.contact.phone_number
        # Сохраняем его в базе
        database.register_user(user_id, name, phone_number)
        bot.send_message(user_id, f'Вы успешно зарегистрировались {name}',
                         reply_markup=telebot.types.ReplyKeyboardRemove())

        # Открываем меню
        products = database.get_pr_name_id()
        bot.send_message(user_id, 'Выберите пункт меню', reply_markup=buttons.menu_menu())

    # если пользователь не отправил контакт
    elif not message.contact:
        bot.send_message(user_id, 'Отправьте контакт с помощью кнопки', reply_markup=buttons.number_buttons())

        # Обратно на этап получения номера
        bot.register_next_step_handler(message, get_number, name)

@bot.message_handler(content_types=['text'])
def menu(message):
    user_id = message.from_user.id
    if message.text == "Log out":
        bot.send_message(user_id, "You logged out", reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text=='Menu':
        bot.send_message(user_id, "Welcome to cafe menu", reply_markup=buttons.menu_menu())
        bot.register_next_step_handler(message, options)

def options(message):
    user_id = message.from_user.id
    if message.text == "Coffee":
        bot.send_message(user_id, "Coffee", reply_markup=buttons.coffee())
        bot.register_next_step_handler(message, coffee)
    elif message.text == "Sweets":
        bot.send_message(user_id, "Sweets", reply_markup=buttons.sweets1())
        bot.register_next_step_handler(message, sweets)
    elif message.text == "Snacks":
        bot.send_message(user_id, "Snacks", reply_markup=buttons.snacks())
        bot.register_next_step_handler(message, snacks)
    elif message.text == "Other":
        pass
    elif message.text == "Back":
        bot.send_message(user_id, 'Welcome', reply_markup=buttons.after_start())
        bot.register_next_step_handler(message, options)
def coffee(message):
    user_id = message.from_user.id
    if message.text == "Americano":
        bot.send_photo(user_id, "https://coffeeatthree.com/wp-content/uploads/hot-americano-recipe.jpg", caption="Americano", reply_markup=buttons.image_buttons())
    elif message.text == "Latte":
        bot.send_photo(user_id, "https://www.caffesociety.co.uk/assets/recipe-images/latte-small.jpg", caption='Latte', reply_markup=buttons.image_buttons())
    elif message.text == "Capuccino":
        bot.send_photo(user_id, "https://www.philips.com/c-dam/b2c/master/experience/ho/philips-chef/recipe/drinks-and-ice-creams/delicious-cappuccino/delicious-cappuccino-thumb.jpg", caption='Capuccino', reply_markup=buttons.image_buttons())
    elif message.text == "Espresso":
        bot.send_photo(user_id, "https://www.nescafe.com/gb/sites/default/files/2023-08/Nes_Web3_Article_Header_Espresso_1448x1240.png", caption="Espresso", reply_markup=buttons.image_buttons())
    elif message.text == "Back":
        bot.send_message(user_id, "Welcome to menu", reply_markup=buttons.menu_menu())
        bot.register_next_step_handler(message, options)

def sweets(message):
    user_id = message.from_user.id
    if message.text == 'Cheesecake':
        bot.send_photo(user_id, "https://coffeeatthree.com/wp-content/uploads/hot-americano-recipe.jpg",
                       caption="Cheesecake", reply_markup=buttons.image_buttons())
    elif message.text == "Donuts":
        bot.send_photo(user_id, "https://www.caffesociety.co.uk/assets/recipe-images/latte-small.jpg", caption='Donuts',
                       reply_markup=buttons.image_buttons())
    elif message.text == "Ecklers":
        bot.send_photo(user_id,
                       "https://www.philips.com/c-dam/b2c/master/experience/ho/philips-chef/recipe/drinks-and-ice-creams/delicious-cappuccino/delicious-cappuccino-thumb.jpg",
                       caption='Ecklers', reply_markup=buttons.image_buttons())
    elif message.text == "Cackes":
        bot.send_photo(user_id,
                       "https://www.nescafe.com/gb/sites/default/files/2023-08/Nes_Web3_Article_Header_Espresso_1448x1240.png",
                       caption="Cakes", reply_markup=buttons.image_buttons())
    elif message.text == "Back":
        bot.send_message(user_id, "Welcome to menu", reply_markup=buttons.menu_menu())
        bot.register_next_step_handler(message, options)

def snacks(message):
    user_id = message.from_user.id
    if message.text == "Sandwich":
        bot.send_photo(user_id, "https://coffeeatthree.com/wp-content/uploads/hot-americano-recipe.jpg",
                       caption="Americano", reply_markup=buttons.image_buttons())
    elif message.text == "Omelette":
        bot.send_photo(user_id, "https://www.caffesociety.co.uk/assets/recipe-images/latte-small.jpg", caption='Latte',
                       reply_markup=buttons.image_buttons())
    elif message.text == "Burger with french fries":
        bot.send_photo(user_id,
                       "https://www.philips.com/c-dam/b2c/master/experience/ho/philips-chef/recipe/drinks-and-ice-creams/delicious-cappuccino/delicious-cappuccino-thumb.jpg",
                       caption='Capuccino', reply_markup=buttons.image_buttons())
    elif message.text == "Espresso":
        bot.send_photo(user_id,
                       "https://www.nescafe.com/gb/sites/default/files/2023-08/Nes_Web3_Article_Header_Espresso_1448x1240.png",
                       caption="Espresso", reply_markup=buttons.image_buttons())
    elif message.text == "Back":
        bot.send_message(user_id, "Welcome to menu", reply_markup=buttons.menu_menu())
        bot.register_next_step_handler(message, options)




@bot.callback_query_handler(lambda call: call.data in ['plus', 'minus', 'to_cart', 'back'])
def get_user_product_count(call):
    user_id = call.message.chat.id

    actual_count = users.get(user_id, {}).get('pr_count', 0)
    # Если пользователь нажал на +
    if call.data == 'plus':
        # Меняем значение кнопки
        # actual_count = users[user_id]['pr_count']
        users[user_id] = users.get(user_id, {})
        users[user_id]['pr_count'] = actual_count + 1
        new_text = f'+{users[user_id]["pr_count"]}'
        bot.edit_message_reply_markup(chat_id=user_id,
                                      message_id=call.message.message_id,
                                      reply_markup=buttons.image_buttons(new_text, actual_count))
    elif call.data == "minus":
        actual_count = users[user_id]['pr_count']
        users[user_id]['pr_count'] -= 1
        bot.edit_message_reply_markup(chat_id=user_id, message_id=call.message.message_id, reply_markup=buttons.image_buttons('minus', actual_count))
    elif call.data == 'to_cart':
        product_count = users[user_id]['pr_count']
        user_product = users[user_id]['pr_name']
        database.add_product_to_cart(user_id, user_product, product_count)

        products = database.get_product_id()

        bot.edit_message_text('Продукт добавлен в корзину', user_id, call.message.message_id,
                              reply_markup=buttons.menu_menu(products)
                              )
    elif call.data == "back":
        bot.register_next_step_handler(call.message, coffee)

@bot.callback_query_handler(lambda call: int(call.data) in database.get_pr_id())
def get_user_product(call):
    # Сохраним айди пользователя
    user_id = call.message.chat.id

    # Сохраним продукт во временный словарь
    # call.data - значение нажатой кнопки(инлайн)
    users[user_id] = {'pr_name': call.data, 'pr_count': 1}
    print(users)

    # Сохраним айди сообщения
    message_id = call.message.message_id

    # Поменять кнопки на выбор количества
    bot.edit_message_text('Выберите количество',
                          chat_id=user_id, message_id=message_id,
                          reply_markup=buttons.image_buttons())

def accept(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "You accept your order: ", reply_markup=buttons.get_accept())
    if message.text == "Подтвердить":
        bot.send_message(user_id, "Your cart", reply_markup=buttons.get_accept())
        bot.register_next_step_handler(message, cart)
    elif message.text == "Отменить":
        bot.send_message(user_id, "Back to the menu", reply_markup=buttons.menu_menu())
        bot.register_next_step_handler(message, options)

def cart(message):
    pass

#"https://www.wholesomeyum.com/wp-content/uploads/2017/03/wholesomeyum-Keto-Cheesecake-Recipe-Low-Carb-Sugar-Free-Cheesecake.jpg"
#"https://vzfk.com.ua/upload/gallery/large/oC.jpg"
#"https://as2.ftcdn.net/v2/jpg/00/55/33/95/1000_F_55339517_X2HjkIkjCpWMiiS1RAM5zssjnkYpW20u.jpg"
#"https://images.pexels.com/photos/291528/pexels-photo-291528.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"





bot.infinity_polling()


