from aiogram.fsm.state import StatesGroup, State


class Order_status(StatesGroup):
    save_username = State()