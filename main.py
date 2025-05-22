import asyncio
import logging

from aiogram import Bot, Dispatcher

from database.core import init_db
from config.settings import settings


async def main():
    # initing  database
    await init_db()

    bot = Bot(token=settings.API_TOKEN)
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")
