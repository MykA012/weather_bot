from aiogram import Router
from . import commands

root_router = Router()

root_router.include_router(commands.router)
