from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import pyperclip

from APP.messages import MESSAGES
import APP.keyboards as kb
import APP.database.requests as rq
from APP.classes import UserDelete

router_basic = Router()

def format_user(user):
    if user['status'] == MESSAGES["not_suitable"]:
        return f"ID:{user['id']}.\nИмя: {user['name']},\nСтатус: {user['status']}\n"
    else:
        return (
            f"ID:{user['id']}.\nИмя: {user['name']},\n"
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

@router_basic.message(F.text == MESSAGES["report"])
async def report(message: Message):
    parent_id= await rq.get_recruit_id_by_tg_id(message.from_user.id)
    users = await rq.get_users(parent_id)
    if users:
        report_message = "\n".join([format_user(user) for user in users])
    else:
        report_message = MESSAGES["no_users"]
    
    await message.answer(report_message, reply_markup=kb.report_btns)

@router_basic.message(F.text == MESSAGES["edit"])
async def edit_data(message: Message):
    await message.answer(MESSAGES["select_edit"], reply_markup=kb.edit)

@router_basic.message(F.text == MESSAGES["delete_person"])
async def del_user_start(message: Message, state: FSMContext):
    await state.set_state(UserDelete.id)
    await message.answer("Введите ID пользователя, которого необходимо удалить.")

@router_basic.message(UserDelete.id)
async def del_user(message: Message, state: FSMContext):
    data = await state.update_data(id=message.text)
    parent_id= await rq.get_recruit_id_by_tg_id(message.from_user.id)
    await rq.delete_user(data["id"], parent_id)
    
    await message.answer(f"Пользователь с ID {data["id"]} удален.")
    await state.clear()

@router_basic.message(F.text == MESSAGES["delete_all_person"])
async def del_user_start(message: Message):
    parent_id= await rq.get_recruit_id_by_tg_id(message.from_user.id)
    await rq.delete_all_users(parent_id)
    await message.answer("Все пользователи удалены.")

@router_basic.message(F.text == MESSAGES["edit_person"])
async def edit_info(message: Message):
    await message.answer("Выберите что хотите изменить", )

@router_basic.message(F.text == MESSAGES["go_back"])
async def back(message: Message):
    await message.answer(MESSAGES["select_action"], reply_markup=kb.main)

@router_basic.callback_query()
async def copy_callback(query: CallbackQuery):
    if query.data == "copy":
        await query.answer()  # Ответим на callback, чтобы Telegram не считал его обработанным
        message = query.message  # Получаем сообщение, к которому привязан callback
        if message.text:
            pyperclip.copy(message.text)  # Копируем текст сообщения в буфер обмена
            await query.message.answer("Текст сообщения скопирован в буфер обмена.")
        else:
            await query.message.answer("Сообщение не содержит текста для копирования.")