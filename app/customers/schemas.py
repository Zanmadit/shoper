from pydantic import BaseModel, ConfigDict, EmailStr

class SCustomers(BaseModel): 
    id: int
    email: EmailStr
    password: str
    

    model_config = ConfigDict(from_attributes=True)