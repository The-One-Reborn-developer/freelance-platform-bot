from sqlalchemy import BigInteger, String, Text, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import Base


class Bid(Base):
    __tablename__ = 'bids'

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_telegram_id: Mapped[BigInteger] = mapped_column(BigInteger)
    city: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Float)

    responses = relationship('Response', back_populates='bid')


class Response(Base):
    __tablename__ = 'responses'

    id: Mapped[int] = mapped_column(primary_key=True)
    bid_id: Mapped[int] = mapped_column(ForeignKey('bids.id'))
    performer_telegram_id: Mapped[BigInteger] = mapped_column(BigInteger)

    bid = relationship('Bid', back_populates='responses')

    __table_args__ = (
        UniqueConstraint('bid_id', 'performer_telegram_id', name='unique_bid_response'),
    )