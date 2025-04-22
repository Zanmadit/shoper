from app.dao.base import BaseDAO
from app.products.models import Products

class ProducsDAO(BaseDAO):
    model = Products