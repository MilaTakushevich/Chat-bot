from aiogram import types


button1 = types.KeyboardButton(text="/Начать_опрос")

keyboard1 = [
    [button1],
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

