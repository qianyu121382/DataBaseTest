from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from DAO.Util import ModelExt

engine = create_engine('mysql+pymysql://root:123456@101.201.51.225/homework')
Base = declarative_base()


class test1(Base,ModelExt):
    __tablename__ = 'test1'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    other = Column(String(255))


Session = sessionmaker(bind=engine)
session = Session()
qry = session.query(test1).all()
for emp in qry:
    print(emp)
