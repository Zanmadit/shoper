from sqlalchemy import Boolean, Computed, DateTime, ForeignKey, Integer, String, JSON, Column, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    order_date = Column(Date, nullable=False)

    customer = relationship("Customers", back_populates="orders")
    product = relationship("Products", back_populates="orders")