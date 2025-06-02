from datetime import datetime, time
import asyncio
import logging

from aiogram import Bot

from database.session import get_user_repo
from services.sync import weather_api


async def send_daily_messages(bot: Bot) -> None:
    target_time = time(9, 0)
    while True:
        now = datetime.now().time()

        if now.hour == time.hour and now.minute == target_time.minute:
            async with get_user_repo() as user_repo:
                users = await user_repo.get_all_users()

            for user in users:
                if user.notifications:
                    try:
                        weather = weather_api.today(
                            city=user.city,
                            latitude=user.latitude,
                            longitude=user.longitude,
                        )

                        message = f"""
{weather["icon"]} Прогноз на сегодня ({weather["name"]})
{weather["description"]}
Температура: {weather["temp"]}°C
Ощущается как {weather["feels_like"]}°C"""

                        await bot.send_message(user.telegram_id, message)

                    except Exception as e:
                        logging.info(
                            f"Error while senfing message user: id = {user.id}: {e}"
                        )

        await asyncio.sleep(30)
