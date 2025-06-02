from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, func

from datetime import datetime

from database.models.base import Base


class User(Base):
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str | None]
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str | None]

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )

    notifications: Mapped[bool] = mapped_column(default=True)

    latitude: Mapped[float | None] = mapped_column(default=None)
    longitude: Mapped[float | None] = mapped_column(default=None)
    city: Mapped[str | None] = mapped_column(default=None)
