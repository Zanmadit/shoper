from datetime import date 
from pydantic import BaseModel, ConfigDict

class SProducts(BaseModel):
    id: int
    name: str
    price: int
    quantity: int

    
    model_config = ConfigDict(from_attributes=True)