from contextlib import asynccontextmanager
from typing import AsyncIterator

from database.core import async_session_maker
from database.repositories.user_repositories import UserRepository


@asynccontextmanager
async def get_user_repo() -> AsyncIterator[UserRepository]:
    async with async_session_maker() as session:
        yield UserRepository(session)
