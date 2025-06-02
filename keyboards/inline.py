from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


notifications = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Включить", callback_data="turn_on_notifications"
            ),
            InlineKeyboardButton(
                text="❌ Выключить", callback_data="turn_off_notifications"
            ),
        ]
    ]
)
