import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🪨 Камень")
    item2 = types.KeyboardButton("✂️ Ножницы")
    item3 = types.KeyboardButton("📄 Бумага")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - "
                     "<b>{1.first_name}</b>, бот созданный для вашей игры.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

# Обработка нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def handle_click(message):
    if message.text == "🪨 Камень":
        play_game(message, "rock")
    elif message.text == "✂️ Ножницы":
        play_game(message, "scissors")
    elif message.text == "📄 Бумага":
        play_game(message, "paper")


# Функция для игры в камень, ножницы, бумагу
def play_game(message, user_choice):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        result = "Ничья! 🤝"
    elif (
        (user_choice == "rock" and bot_choice == "scissors") or
        (user_choice == "scissors" and bot_choice == "paper") or
        (user_choice == "paper" and bot_choice == "rock")
    ):
        result = "Вы победили! 🎉"
    else:
        result = "Вы проиграли! 😞"

    bot.send_message(message.chat.id, f"Вы выбрали {user_choice.capitalize()}, "
                                      f"бот выбрал {bot_choice.capitalize()}. {result}")

# Добавьте обработку других команд и функции, если нужно

# Запуск бота
bot.polling(none_stop=True)