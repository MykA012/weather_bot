from sqlalchemy import select, update

from database.models.user import User
from database.repositories.base import CRUDBase


class UserRepository(CRUDBase):
    async def get_by_telegram_id(self, telegram_id) -> User | None:
        stmt = select(User).where(User.telegram_id == telegram_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all_users(self) -> list[User] | None:
        stmt = select(User)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(
        self,
        telegram_id: int,
        first_name: str,
        username: str | None = None,
        last_name: str | None = None,
    ) -> User | None:
        user = await self.get_by_telegram_id(telegram_id)
        if not user:
            user = User(
                telegram_id=telegram_id,
                first_name=first_name,
                username=username,
                last_name=last_name,
            )
            self.session.add(user)
            await self.commit()
            return user
        return None

    async def set_location(
        self,
        telegram_id: int,
        city: str = None,
        latitude: float = None,
        longitude: float = None,
    ) -> bool:
        stmt = (
            update(User)
            .where(User.telegram_id == telegram_id)
            .values(city=city, latitude=latitude, longitude=longitude)
        )
        result = await self.session.execute(stmt)
        await self.commit()
        return result.rowcount > 0

    async def notifications_change(self, telegram_id: int, status: bool) -> bool:
        stmt = (
            update(User)
            .where(User.telegram_id == telegram_id)
            .values(notifications=status)
        )
        result = await self.session.execute(stmt)
        await self.commit()
        return result.rowcount > 0
