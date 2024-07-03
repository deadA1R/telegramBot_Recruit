from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='Добавить человека🟢')],
                                    [KeyboardButton(text='Редактировать🟢'), KeyboardButton(text='Отчет🟢')],
                                ], resize_keyboard=True, input_field_placeholder="Выберите пункт меню")

edit = ReplyKeyboardMarkup(keyboard=[
                                [KeyboardButton(text='Изменить данные человека', )], 
                                [KeyboardButton(text='Удалить человека🟢'), KeyboardButton(text='Очистить список людей')],
                                [KeyboardButton(text='На главную🟢')]
                                ], resize_keyboard=True, input_field_placeholder="Выберите что хотите отредактировать")


get_number_recruit = ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='Отправить номер', request_contact=True)],
                                ], resize_keyboard=True, input_field_placeholder="Введите номер")

set_status_user = ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='Подходит'), KeyboardButton(text='Не подходит')],
                                ], resize_keyboard=True, input_field_placeholder="Выберите статус")

set_work_status = ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text='Есть опыт работы'), KeyboardButton(text='Опыта работы нет')],
                                ], resize_keyboard=True, input_field_placeholder="Выберите статус")

