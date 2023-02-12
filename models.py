from sqlalchemy import Column, Integer, Float
from database import Base


# Define the account model
class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    balance = Column(Float)

# Define the transfer model
class Transfer(Base):
    __tablename__ = 'transfers'

    source_id = Column(Integer, primary_key=True)
    target_id = Column(Integer)
    amount = Column(Float)