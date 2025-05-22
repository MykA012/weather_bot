from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls: str) -> str:
        return cls.__name__.lower() + "s"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
