from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards import reply

from database.session import get_user_repo


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    async with get_user_repo() as user_repo:
        user = await user_repo.create(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            username=message.from_user.username,
            last_name=message.from_user.last_name,
        )
        if not user:
            await message.answer(
                "Привет! Для получения погоды используйте кнопки ниже.",
                reply_markup=reply.main,
            )
            return

        await message.answer(
            "☔️ Для предоставления информации о погоде боту необходимо знать город, в котором вы находитесь. Поделитесь местоположением или отправьте боту название вашего города",
            reply_markup=reply.provide_location,
        )


@router.message(F.location)
async def handle_location(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    async with get_user_repo() as user_repo:
        request = await user_repo.set_location(
            telegram_id=message.from_user.id, latitude=latitude, longitude=longitude
        )
        await message.answer("Теперь вы можете использовать все возможности бота!", reply_markup=reply.main)
