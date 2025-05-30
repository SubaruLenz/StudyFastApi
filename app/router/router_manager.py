from fastapi import APIRouter
from . import test_table, jwt

routerManager = APIRouter()
routerManager.include_router(test_table.router)
routerManager.include_router(jwt.router)