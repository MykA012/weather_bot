import asyncio
import logging

from aiogram import Bot, Dispatcher

from database.core import init_db
from config.settings import settings
from handlers import root_router
from services.async_.daily_messages import send_daily_messages


async def main():
    # initing  database
    await init_db()

    bot = Bot(token=settings.API_TOKEN)
    dp = Dispatcher()
    dp.include_router(root_router)

    asyncio.create_task(send_daily_messages(bot))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")
