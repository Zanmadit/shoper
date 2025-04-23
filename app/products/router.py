from fastapi import APIRouter

from app.products.dao import ProductsDAO
from app.products.models import Products

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("")
async def get_all_products():
    return await ProductsDAO.find_all()