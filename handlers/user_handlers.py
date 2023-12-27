import logging

from support.logger import log

from aiogram import Router, F
from aiogram.filters import Command, StateFilter, CommandStart, and_f, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from keyboards.order_keyboard import *
from fnAPI.fn_api import get_fn_user_info
from database.db_manipulations import UsersDB

db = UsersDB()
from handlers import Order_status

# Инициализируем роутер уровня модуля
router = Router()

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage = MemoryStorage()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):

    await message.answer(text=
                         'Fn nickname:')
    await state.set_state(Order_status.save_username)


# Обробка запиту з кнопки назад

@router.message(F.text == 'Оновити стату')
async def update_start_bot(message: Message, state: FSMContext):
    username = db.get_user_order_number(message.from_user.id)
    ans = get_fn_user_info(username)
    await message.answer(text=ans, reply_markup=back_button_keyboard())
    await state.clear()


@router.message(F.text == 'Оновити нікнейм')
async def update_nickname(message: Message, state: FSMContext):
    await message.answer(text='Fn nickname:')
    await state.set_state(Order_status.save_username)


@router.message(StateFilter(Order_status.save_username))
async def ping_fn(message: Message, state: FSMContext):
    db.process_user(message.from_user.id, message.text)
    await message.answer(text="Нікнейм збережено", reply_markup=back_button_keyboard())
    username = db.get_user_order_number(message.from_user.id)
    ans = get_fn_user_info(username)
    await message.answer(text=ans, reply_markup=back_button_keyboard())
    await state.clear()


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='/help')
