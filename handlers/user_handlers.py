from aiogram import Router, F
from aiogram.filters import Command, StateFilter, CommandStart, and_f, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from keyboards.order_keyboard import *
from fnAPI.fn_api import get_fn_user_info
from support.filters import alpha_space_filter

# Инициализируем роутер уровня модуля
router = Router()

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage = MemoryStorage()


#  "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=
                         'Fn nickname:')


@router.message()
async def ping_fn(message: Message, state: FSMContext):
    await message.answer(text=get_fn_user_info(message.text))


# Обробка запиту з кнопки назад

@router.message(F.text == 'Назад  🔙')
async def update_start_bot(message: Message, state: FSMContext):
    await message.answer(text='Головне меню', reply_markup=back_button_keyboard())
    await state.clear()


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='/help')
