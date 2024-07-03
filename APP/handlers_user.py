from aiogram import F, Router
from aiogram.types import Message 
from aiogram.fsm.context import FSMContext

from APP.classes import UserAdd
import APP.keyboards as kb
import APP.database.requests as rq

router_usr = Router()


MESSAGES = {
    "thanks": "Спасибо, претендент добавлен",
    "add_person": "Добавить человека🟢",
    "set_status": "Выберите статус",
    "enter_age": "Введите возраст",
    "enter_address": "Введите адрес",
    "enter_phone_number": "Введите номер телефона",
    "add_comment": "Добавьте дополнительный комментарий",
    "main_menu": "Выберите действие",
    "no_experience": "Опыта работы нет",
    "not_suitable": "Не подходит",
}

@router_usr.message(F.text == MESSAGES["add_person"])
async def add_user(message: Message, state: FSMContext):
    await state.set_state(UserAdd.name)
    await message.answer("Введите имя потенциального сотрудника")

@router_usr.message(UserAdd.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserAdd.status)
    await message.answer(MESSAGES["set_status"], reply_markup=kb.set_status_user)

@router_usr.message(UserAdd.status)
async def add_status(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    if message.text == MESSAGES["not_suitable"]:
        data = await state.get_data()
        await rq.set_user_not_releable(data)
        await message.answer(MESSAGES["thanks"], reply_markup=kb.main)
        await state.clear()
    else:
        await state.set_state(UserAdd.age)
        await message.answer(MESSAGES["enter_age"])

@router_usr.message(UserAdd.age)
async def add_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserAdd.address)
    await message.answer(MESSAGES["enter_address"])

@router_usr.message(UserAdd.address)
async def add_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await state.set_state(UserAdd.number)
    await message.answer(MESSAGES["enter_phone_number"])

@router_usr.message(UserAdd.number)
async def add_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(UserAdd.previous_work_status)
    await message.answer(MESSAGES["set_status"], reply_markup=kb.set_work_status)

@router_usr.message(UserAdd.previous_work_status)
async def add_previous_work_status(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == MESSAGES["no_experience"]:
        await state.update_data(previous_work_status=message.text)
        await state.set_state(UserAdd.comment)
        await message.answer(MESSAGES["add_comment"])
    else:
        await state.update_data(previous_work_status=message.text)
        await state.set_state(UserAdd.previous_work_discription)
        await message.answer("Введите коментарий по опыту работы")

@router_usr.message(UserAdd.previous_work_discription)
async def add_previous_work_discription(message: Message, state: FSMContext):
    await state.update_data(previous_work_discription=message.text)
    await state.set_state(UserAdd.comment)
    await message.answer(MESSAGES["add_comment"])

@router_usr.message(UserAdd.comment)
async def add_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    if not data.get("previous_work_discription"):
        data["previous_work_discription"] = "-"
    await message.answer(MESSAGES["thanks"], reply_markup=kb.main)
    await rq.set_user(data)
    await state.clear()