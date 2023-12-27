from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
back_button = KeyboardButton(text='Оновити стату')
save_nickname_btn = KeyboardButton(text='Оновити нікнейм')






def back_button_keyboard() -> ReplyKeyboardMarkup:
    button = back_button

    keyboard = ReplyKeyboardMarkup(keyboard=[[button], [save_nickname_btn]], resize_keyboard=True)
    return keyboard

