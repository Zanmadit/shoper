from datetime import date 
from pydantic import BaseModel, ConfigDict

class SOrders(BaseModel):
    id: int
    customer_id: int
    product_id: int
    quantity: int
    order_date: date

    
    model_config = ConfigDict(from_attributes=True)