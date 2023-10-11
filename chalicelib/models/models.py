from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os


Base = declarative_base()

class UnitMeasure(Base):
    __tablename__ = 'unit_measure'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    unit_measure_id = Column(Integer, ForeignKey('unit_measure.id'), nullable=False)
    unit_measure = relationship('UnitMeasure', backref='products')


class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', backref='sales')


# connect to database
db_uri = os.environ["SQLALCHEMY_DATABASE_URI"]
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)