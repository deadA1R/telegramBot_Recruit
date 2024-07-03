from aiogram.fsm.state import State, StatesGroup

class UserAdd(StatesGroup):
    name = State()
    status = State()
    age = State()
    address = State()
    number = State()
    previous_work_status = State()
    previous_work_discription = State()
    comment = State()

class RecruitRegistration(StatesGroup):
    name = State()
    number = State()

class UserDelete(StatesGroup):
    id = State()