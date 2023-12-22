from aiogram.fsm.state import StatesGroup, State


class Order_status(StatesGroup):
    status_by_phone_number = State()
    status_by_order_number = State()
    waiting_order_status = State()
