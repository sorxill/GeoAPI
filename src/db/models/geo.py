"""ORM show Geo table."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Geo(Base):
    """Represent table geo for address."""

    __tablename__ = "geo"

    address: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        nullable=False,
        default="Unknown",
    )
    geo: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    # Не взял тип данных Point в связи с отсутствием надобности манипуляции над данными.

    def __repr__(self) -> str:
        """Def for representation"""
        return f"Geo(address={self.address!r}, geo={self.geo!r})"
