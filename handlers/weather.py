from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "Погода сейчас")
async def weather_now(message: Message):
    # db request
    pass
