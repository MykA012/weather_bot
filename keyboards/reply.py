from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Погода сейчас")],
        [KeyboardButton(text="Погода завтра")],
        [KeyboardButton(text="Погода на неделю")],
        [KeyboardButton(text="Сменить локацию")]
    ]
)