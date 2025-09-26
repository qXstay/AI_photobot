from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_back_to_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
        resize_keyboard=True,
        one_time_keyboard=True
    )