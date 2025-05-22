from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self):
        await self.session.commit()

    async def refresh(self, entity):
        await self.session.refresh(entity)
