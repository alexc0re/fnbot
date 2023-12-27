from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
back_button = KeyboardButton(text='Оновити стату')
help_btn = KeyboardButton(text='/help')
this_season_text = KeyboardButton(text='Стата за цей сезон')







def back_button_keyboard() -> ReplyKeyboardMarkup:
    button = back_button

    keyboard = ReplyKeyboardMarkup(keyboard=[[button], [this_season_text], [help_btn]], resize_keyboard=True)
    return keyboard

