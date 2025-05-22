from aiogram.fsm.state import StatesGroup, State


class Start_States(StatesGroup):
    waiting_for_city = State()