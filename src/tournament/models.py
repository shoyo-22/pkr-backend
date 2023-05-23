from sqlalchemy import Column, String

from ..db.database import Base

class Tournaments(Base):
    __tablename__ = 'tournaments'

    id = Column(String)
    name = Column(String)
    logo = Column(String)
    datetime = Column(String)
    location = Column(String)
    league = Column(String)
    fraction = Column(String)
    status = Column(String)
    judge = Column(String)
    link = Column(String)
