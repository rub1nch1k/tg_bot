import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message

class Bot(telebot.TeleBot):
    def __init__(self, token):
        super()__init__(token)
        self.featuresMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        self.featuresMarkup.add(
            KeyboardButton(😎'Взлом пентагона'), 
            KeyboardButton(🧮'Калькулятор'),
            KeyboardButton(🎮'9 жизней'),
            KeyboardButton(🎬'Поиск видео'),
            KeyboardButton(🎭'Рандомный стикер'),
            KeyboardButton(📋'Информация')
        )
        