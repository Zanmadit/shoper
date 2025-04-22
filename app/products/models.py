from sqlalchemy import Boolean, Computed, DateTime, ForeignKey, Integer, String, JSON, Column, Date
from sqlalchemy.orm import relationship
import datetime

from app.database import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True) #UUID
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=True)
    
    orders = relationship("Order", back_populates="product")