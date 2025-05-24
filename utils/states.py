from aiogram.fsm.state import StatesGroup, State


class UserLocationStates(StatesGroup):
    waiting_for_loc = State()
