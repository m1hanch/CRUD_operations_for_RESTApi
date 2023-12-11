from sqlalchemy import String, Date, Column, Integer

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    email = Column(String(150), index=True, unique=True)
    phone = Column(String(17))
    birthday = Column(Date)
    other = Column(String)

