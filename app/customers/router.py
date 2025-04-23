from fastapi import APIRouter, Response, Depends

from app.customers.dao import CustomersDAO
from app.customers.schemas import SCustomers
from app.customers.models import Customers
from app.exceptions import UserALreadyExistsException, IncorrectEmailOrPasswordException
from app.customers.auth import get_password_hash, authentificate_user, create_access_token
from app.customers.dependencies import get_current_user

router = APIRouter(
    prefix="/customers",
    tags = ["Customers"]
)

@router.post("/register")
async def register_user(user_data: SCustomers):
    existing_user = await CustomersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserALreadyExistsException
    
    hashed_password = get_password_hash(user_data.password)
    await CustomersDAO.add(email=user_data.email, hashed_password=hashed_password)

@router.post('/login')
async def login_user(responce: Response, user_data: SCustomers):
    user = await authentificate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    responce.set_cookie("order_access_token", access_token, httponly=True)
    return access_token

@router.post("/logout")
async def logout_user(responce: Response):
    responce.delete_cookie("order_access_token")


@router.get("/me")
async def read_users_me(current_user: Customers = Depends(get_current_user)):
    return current_user