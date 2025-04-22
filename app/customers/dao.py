from app.dao.base import BaseDAO
from app.customers.models import Customers

class CustomersDAO(BaseDAO):
    model = Customers