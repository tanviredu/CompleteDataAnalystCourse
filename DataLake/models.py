from sqlalchemy                 import Column,Integer,String,DateTime,Float
from sqlalchemy.ext.declarative import declarative_base
from datetime                   import datetime

Base = declarative_base()

class Data(Base):
    __tablename__ = "Data"

    id        = Column(Integer,primary_key=True,autoincrement=True)
    timestamp = Column(DateTime,default=datetime.utcnow,nullable=False)
    value     = Column(Float,default=0.0)

