from fastapi import APIRouter

from app.orders.dao import OrdersDAO
from app.orders.models import Orders

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.get("")
async def get_order():
    return await OrdersDAO.find_all(id=1)