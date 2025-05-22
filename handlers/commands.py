from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    # user registration in db if necessary

    await message.answer("Привет! Для получения погоды используйте кнопки ниже.", reply_markup=reply.main)


