from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from aiogram.fsm.context import FSMContext

from keyboards import reply
from database.session import get_user_repo
from utils.states import UserLocationStates
from services.sync import weather_api

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    async with get_user_repo() as user_repo:
        user = await user_repo.get_by_telegram_id(message.from_user.id)

        if user and (user.city or user.lat):
            await message.answer(
                "Привет! Для получения погоды используйте кнопки ниже.",
                reply_markup=reply.main,
            )
            return
        elif not user:
            user = await user_repo.create(
                telegram_id=message.from_user.id,
                first_name=message.from_user.first_name,
                username=message.from_user.username,
                last_name=message.from_user.last_name,
            )

        await state.set_state(UserLocationStates.waiting_for_loc)
        await message.answer(
            "☔️ Для предоставления информации о погоде боту необходимо знать город, в котором вы находитесь. Поделитесь местоположением или отправьте боту название вашего города",
            reply_markup=reply.provide_location,
        )


@router.message(UserLocationStates.waiting_for_loc)
async def handle_location(message: Message, state: FSMContext):
    async with get_user_repo() as user_repo:

        if message.location:
            location = message.location
            latitude = location.latitude
            longitude = location.longitude

            await user_repo.set_location(
                telegram_id=message.from_user.id, latitude=latitude, longitude=longitude
            )

        elif message.text:
            city = message.text.strip()

            await user_repo.set_location(telegram_id=message.from_user.id, city=city)

        await state.clear()

        await message.answer(
            "Теперь вы можете использовать все возможности бота!",
            reply_markup=reply.main,
        )
