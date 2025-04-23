from fastapi import FastAPI

from app.orders.router import router as router_orders
from app.products.router import router as router_products
from app.customers.router import router as router_customers

app = FastAPI()

app.include_router(router_orders)
app.include_router(router_products)
app.include_router(router_customers)