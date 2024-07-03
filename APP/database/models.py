from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import os
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url=os.getenv('SQL_URL'))

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Recruit(Base):
    __tablename__ = "recruits"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    tg_id = mapped_column(BigInteger)
    name = mapped_column(String(25))
    number = mapped_column(String(16))

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    status: Mapped[str] = mapped_column(String(15))
    age: Mapped[int] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(String(40), nullable=True)
    number: Mapped[str] = mapped_column(String(16), nullable=True)
    previous_work_status: Mapped[str] = mapped_column(String(20), nullable=True)
    previous_work_discription: Mapped[str] = mapped_column(String(120), nullable=True)
    comment: Mapped[str] = mapped_column(String(120), nullable=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey('recruits.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
