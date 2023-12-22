import time

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.order_keyboard import find_by_phone_number_button, back_button_keyboard, watch_order_keyboard, \
    phone_or_order_number_buttons
from support.texts import WAIT_ORDER_STATUS_TEXT


async def process_status(status, response_message, message: Message, state: FSMContext):
    if status in ["Error", "Not found"]:
        await message.answer(text=str(response_message), reply_markup=find_by_phone_number_button())
        await state.clear()

    elif status in ["pending", "paid", "custom-112812", "received"]:
        await message.answer(text=str(response_message), reply_markup=back_button_keyboard())
        await state.clear()
        time.sleep(5)
        await message.answer(text=WAIT_ORDER_STATUS_TEXT, reply_markup=watch_order_keyboard())

    elif status in ["canceled", "delivered"]:
        await message.answer(text=str(response_message), reply_markup=phone_or_order_number_buttons())
        await state.clear()