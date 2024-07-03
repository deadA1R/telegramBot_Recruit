from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from APP.messages import MESSAGES

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MESSAGES["add_person"])],
    [KeyboardButton(text=MESSAGES["edit"]), KeyboardButton(text=MESSAGES["report"])],
], resize_keyboard=True, input_field_placeholder=MESSAGES["choose_menu"])

edit = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MESSAGES["edit_person"], )], 
    [KeyboardButton(text=MESSAGES["delete_person"]), KeyboardButton(text=MESSAGES["delete_all_person"])],
    [KeyboardButton(text=MESSAGES["go_back"],)]
], resize_keyboard=True, input_field_placeholder=MESSAGES["set_default"])

get_number_recruit = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MESSAGES["send_number"], request_contact=True)],
], resize_keyboard=True, input_field_placeholder=MESSAGES["set_number"])

set_status_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MESSAGES["suitable"]), KeyboardButton(text=MESSAGES["not_suitable"])],
], resize_keyboard=True, input_field_placeholder=MESSAGES["set_status"])

set_work_status = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=MESSAGES["experience"]), KeyboardButton(text=MESSAGES["no_experience"])],
], resize_keyboard=True, input_field_placeholder=MESSAGES["set_status"])

report_btns = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Копировать", callback_data="copy"), InlineKeyboardButton(text="Отправить в чат", callback_data="send_to_wp")]
])

