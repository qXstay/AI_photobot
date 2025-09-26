from aiogram.fsm.state import State, StatesGroup

class PhotoStates(StatesGroup):
    waiting_for_photo = State()
    waiting_for_prompt_choice = State()
    waiting_for_custom_prompt = State()