from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
back_button = KeyboardButton(text='Назад  🔙')




def back_button_keyboard() -> ReplyKeyboardMarkup:
    button = back_button
    keyboard = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
    return keyboard

