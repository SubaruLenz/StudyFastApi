import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, MappedColumn

from .database import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = MappedColumn(Integer, unique=True, primary_key=True, nullable=False)
    username: Mapped[str] = MappedColumn(String(255), unique=True, nullable=False)
    password: Mapped[str] = MappedColumn(String(255), nullable=False)
    create_date: Mapped[datetime.datetime] = MappedColumn(DateTime, default=datetime.datetime.now)

class TestTable(Base):
    __tablename__ = "test_table"

    id: Mapped[int] = MappedColumn(Integer, unique=True, primary_key=True, nullable=False)
    title: Mapped[str] = MappedColumn(String)
    body: Mapped[str] = MappedColumn(String)