from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Погода сейчас")],
        [KeyboardButton(text="Погода завтра")],
        [KeyboardButton(text="Сменить локацию"), KeyboardButton(text="Уведомления")],
    ],
    resize_keyboard=True,
)


provide_location = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Поделиться городом", request_location=True)]],
    resize_keyboard=True,
    one_time_keyboard=True,
)
