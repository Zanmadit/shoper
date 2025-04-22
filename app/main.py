from fastapi import FastAPI

from app.orders.router import router as router_orders

app = FastAPI()

app.include_router(router_orders)