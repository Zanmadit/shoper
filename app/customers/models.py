from sqlalchemy import Boolean, Computed, DateTime, ForeignKey, Integer, String, JSON, Column, Date
from sqlalchemy.orm import relationship
import datetime

from app.database import Base

class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True) #UUID
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    orders = relationship("Order", back_populates="customer")