from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, func

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

    latitude: Mapped[float | None]
    longitude: Mapped[float | None]

    city: Mapped[str | None]
