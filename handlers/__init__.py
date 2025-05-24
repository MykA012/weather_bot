from aiogram import Router
from . import commands, weather_cmds

root_router = Router()

root_router.include_router(commands.router)
root_router.include_router(weather_cmds.router)
