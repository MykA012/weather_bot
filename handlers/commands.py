from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext

from keyboards import reply, inline
from database.session import get_user_repo
from utils.states import UserLocationStates
from services.sync.weather_api import validate_city

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    async with get_user_repo() as user_repo:
        user = await user_repo.get_by_telegram_id(message.from_user.id)

        if user and (user.city or user.latitude):
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


@router.message(F.text == "Сменить локацию")
async def change_location(message: Message, state: FSMContext):
    await state.set_state(UserLocationStates.waiting_for_loc)
    await message.answer(
        "Отправь своё место положение для изменения.",
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

            if not validate_city(city):
                await message.answer("Такого города не существует! Попробуйте снова")
                return

            await user_repo.set_location(telegram_id=message.from_user.id, city=city)

        await state.clear()

        await message.answer(
            "Привет! Для получения погоды используйте кнопки ниже.",
            reply_markup=reply.main,
        )


@router.message(F.text == "💬 Уведомления")
async def notifications_status(message: Message):
    async with get_user_repo() as user_repo:
        user = await user_repo.get_by_telegram_id(message.from_user.id)

        if user.notifications:
            status = "Включены"
        else:
            status = "Выключены"

        await message.answer(
            f"Сейчас уведомления {status}", reply_markup=inline.notifications
        )


@router.callback_query(F.data.in_(["turn_on_notifications", "turn_off_notifications"]))
async def turn_on_notifications(callback: CallbackQuery):
    async with get_user_repo() as user_repo:
        if callback.data == "turn_on_notifications":
            status = True
        else:
            status = False

        await user_repo.notifications_change(
            telegram_id=callback.from_user.id, status=status
        )

        await callback.answer()
        await callback.message.answer(
            f"Уведомления {"Включены" if status else "Выключены"}",
            reply_markup=reply.main,
        )
