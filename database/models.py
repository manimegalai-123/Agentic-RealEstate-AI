from sqlalchemy import Column, Integer, String
from database.database import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)

    owner_name = Column(String)
    phone = Column(String)

    location = Column(String)
    area = Column(Integer)

    price = Column(Integer)

    description = Column(String)

    poster_path = Column(String)