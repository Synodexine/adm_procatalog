from fastapi import APIRouter

from .endpoints.products import router as products_router


api_router = APIRouter(
    prefix='/api'
)
api_router.include_router(products_router)
