from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Погода сейчас")],
        [KeyboardButton(text="Погода завтра")],
        [KeyboardButton(text="Погода на неделю")],
        [KeyboardButton(text="Сменить локацию")],
    ],
    resize_keyboard=True,
)


provide_location = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Поделиться городом")]],
    resize_keyboard=True,
    one_time_keyboard=True,
)
