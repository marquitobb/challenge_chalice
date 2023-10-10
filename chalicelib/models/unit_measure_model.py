from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


Base = declarative_base()

class UnitMeasure(Base):
    __tablename__ = 'unit_measure'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

db_uri = os.environ["SQLALCHEMY_DATABASE_URI"]
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)