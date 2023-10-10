from .database import Base
from sqlalchemy import Column, Integer, String


class Tournament(Base):
    __tablename__ = 'tournament'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    time = Column(String, nullable=False)
    location = Column(String, nullable=False)
    league = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    main_referee = Column(String, nullable=False)
    level = Column(String, nullable=False)
    language = Column(String, nullable=False)
    link = Column(String, nullable=False)
    format = Column(String, nullable=False)
    fraction = Column(String, nullable=False)
    referee = Column(String, nullable=False)
