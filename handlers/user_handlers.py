from aiogram import Router, F
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from keyboards.order_keyboard import *
from api.fn_api import get_fn_user_info
from api.fn_downdetector import get_fortnite_statuses_ua
from database.db_manipulations import UsersDB

db = UsersDB()
from handlers import Order_status

router = Router()
storage = MemoryStorage()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text='Fn nickname:')
    await state.set_state(Order_status.save_username)


@router.message(F.text == 'Оновити стату')
async def update_start_bot(message: Message, state: FSMContext):
    username = db.get_user_order_number(message.from_user.id)
    ans = get_fn_user_info(username)
    await message.answer(text=ans, reply_markup=back_button_keyboard())
    await state.clear()


@router.message(Command(commands='new'))
async def update_nickname(message: Message, state: FSMContext):
    await message.answer(text='Fn nickname:')
    await state.set_state(Order_status.save_username)


@router.message(StateFilter(Order_status.save_username))
async def ping_fn(message: Message, state: FSMContext):
    db.process_user(message.from_user.id, message.text)
    await message.answer(text="Нікнейм збережено", reply_markup=back_button_keyboard())
    username = db.get_user_order_number(message.from_user.id)
    ans = get_fn_user_info(username)
    await message.answer(text=ans, reply_markup=back_button_keyboard())
    await state.clear()


@router.message(F.text == 'Стата за цей сезон')
async def last_season_stat(message: Message, state: FSMContext):
    username = db.get_user_order_number(message.from_user.id)
    ans = get_fn_user_info(username, "season")
    await message.answer(text=ans, reply_markup=back_button_keyboard())


@router.message(F.text == 'Статус Fortnite')
async def Status(message: Message, state: FSMContext):
    try:
        statuses = get_fortnite_statuses_ua()

        ans = (
            "Статус Fortnite\n\n"
            f"Друзі, групи та повідомлення: {statuses.get('Друзі, групи та повідомлення', 'Невідомо')}\n"
            f"Голосовий чат: {statuses.get('Голосовий чат', 'Невідомо')}\n"
            f"Пошук матчу: {statuses.get('Пошук матчу', 'Невідомо')}"
        )

        await message.answer(text=ans, reply_markup=back_button_keyboard())
    except Exception as e:
        await message.answer(
            text=f"Не вдалося отримати статус Fortnite: {e}",
            reply_markup=back_button_keyboard()
        )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='/new - змінити нікнейм\n')