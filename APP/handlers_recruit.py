from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message 
from aiogram.fsm.context import FSMContext

import APP.keyboards as kb
import APP.database.requests as rq
from APP.classes import RecruitRegistration

router_recruit = Router()


@router_recruit.message(CommandStart())
async def start_with_reg(message: Message):
    await rq.set_recruit(message.from_user.id)
    await message.answer("Добро пожаловать!", reply_markup=kb.main)

@router_recruit.message(Command("reg"))
async def reg(message: Message, state: FSMContext):
    await state.set_state(RecruitRegistration.name)
    await message.answer("Введите имя")

@router_recruit.message(RecruitRegistration.name)
async def reg_add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RecruitRegistration.number)
    await message.answer("Введите номер", reply_markup=kb.get_number_recruit)

@router_recruit.message(RecruitRegistration.number, F.contact)
async def reg_add_num(message: Message, state: FSMContext):
    await state.update_data(number = message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Спасибо, регистрация завершена\n ", reply_markup=kb.main)
    await state.clear()


