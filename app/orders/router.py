from fastapi import APIRouter

from app.orders.dao import OrdersDAO
from app.orders.models import Orders

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.get("")
async def get_order():
    return await OrdersDAO.find_all()

@router.get("/{order_id}/orders")
async def get_rooms(order_id: int = Orders.id):
    return await OrdersDAO.find_by_id(order_id)