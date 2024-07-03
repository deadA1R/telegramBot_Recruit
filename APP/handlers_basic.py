from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import APP.keyboards as kb
import APP.database.requests as rq
from APP.classes import UserDelete

router_basic = Router()


MESSAGES = {
    "help": "Help message!",
    "no_users": "Нет данных пользователей.",
    "select_action": "Выберите действие",
    "select_edit": "Выберите что хотите изменить"
}

def format_user(user):
    if user['status'] == "Не подходит":
        return f"{user['id']}. Имя: {user['name']},\nСтатус: {user['status']}\n"
    else:
        return (
            f"{user['id']}. Имя: {user['name']},\n"
            f"Статус: {user['status']},\n"
            f"Возраст: {user['age']},\n"
            f"Адрес: {user['address']},\n"
            f"Номер: {user['number']},\n"
            f"Опыт работы: {user['previous_work_status']}, {user['previous_work_discription']},\n"
            f"Дополнительный коментарий: {user["comment"]}\n"
        )

@router_basic.message(Command("help"))
async def help(message: Message):
    await message.reply(MESSAGES["help"])

@router_basic.message(F.text == "Отчет🟢")
async def report(message: Message):
    users = await rq.get_users()
    if users:
        report_message = "\n".join([format_user(user) for user in users])
    else:
        report_message = MESSAGES["no_users"]
    
    await message.answer(report_message)

@router_basic.message(F.text == "Редактировать🟢")
async def edit_data(message: Message):
    await message.answer(MESSAGES["select_edit"], reply_markup=kb.edit)

@router_basic.message(F.text == "Удалить человека🟢")
async def del_user_start(message: Message, state: FSMContext):
    await state.set_state(UserDelete.id)
    await message.answer("Введите ID пользователя, которого необходимо удалить.")

@router_basic.message(UserDelete.id)
async def del_user(message: Message, state: FSMContext):
    data = await state.update_data(id=message.text)
    await rq.delete_user(data["id"])
    
    await message.answer(f"Пользователь с ID {data["id"]} удален.")
    await state.clear()


@router_basic.message(F.text == "На главную🟢")
async def back(message: Message):
    await message.answer(MESSAGES["select_action"], reply_markup=kb.main)
