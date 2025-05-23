from aiogram import Router, F
from aiogram.types import Message

from database.session import get_user_repo

router = Router()


@router.message(F.text == "Погода сейчас")
async def weather_now(message: Message):
    async with get_user_repo() as user_repo:
        user = await user_repo.get_by_telegram_id(message.from_user.id)

        