import telebot
import json

TOKEN = "7161247285:AAENk5FOAvH25uK1pLlW1hHhy4YNCFHT7Kg"
GROUP_ID = "-4105592468"

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(func=lambda message: message.text == "Оставить заявку")
def request_name(message):
    user = dict()
    bot.reply_to(message, "Введите ваше имя:")
    bot.register_next_step_handler(message, request_surname, user)

def request_surname(message, user):
    user["name"] = message.text
    bot.send_message(message.chat.id, "Введите вашу фамилию:")
    msg = bot.register_next_step_handler(message, request_patronymic, user)

def request_patronymic(message, user):
    user["surname"] = message.text
    bot.send_message(message.chat.id, "Введите ваше отчество (Если его нет отправьте точку):")
    bot.register_next_step_handler(message, request_phone, user)

def request_phone(message, user):
    user["patronymic"] = message.text
    bot.send_message(message.chat.id, "Введите ваш номер телефона:")
    bot.register_next_step_handler(message, finish_request, user)

def finish_request(message, user):
    user["phone"] = message.text
    bot.send_message(message.chat.id, "Заявка успешно оставлена!")
    bot.send_message(GROUP_ID, 
    f"""
    Поступила заявка🚐✅
    Имя: {user["name"]}
    Фамилия: {user["surname"]}
    Отчество{": " + user["patronymic"] if user["patronymic"] != "." else " отсутсвует"}
    Номер телефона: {user["phone"]}
    """
    )

@bot.message_handler(func=lambda message: message.chat.type == 'private')
def send_message_to_group(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton(text="Оставить заявку")
    keyboard.add(button)
    bot.send_message(message.chat.id, "Добро пожаловать! Нажмите на кнопку 'Оставить заявку' для заполнения заявки.", reply_markup=keyboard)

bot.polling()