from typing import Any, List, Optional

from fastapi import Depends, Response
from fastapi.routing import APIRouter
from pydantic.types import UUID4

from orders_api.db import models
from orders_api.db.schemas import Product, ProductCreate, ProductUpdate
from orders_api.services import ProductsService, get_products_service

router = APIRouter(prefix="/products")


@router.get("/", response_model=List[Product])
async def list_products(
    product_service: ProductsService = Depends(get_products_service),
) -> List[models.Product]:
    return product_service.list()


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: UUID4, product_service: ProductsService = Depends(get_products_service)
) -> Optional[models.Product]:
    return product_service.get(product_id)


@router.post(
    "/",
    response_model=Product,
    status_code=201,
    responses={
        400: {"description": "Invalid store reference"},
        409: {"description": "Conflict Error"},
    },
)
async def create_product(
    product: ProductCreate,
    product_service: ProductsService = Depends(get_products_service),
) -> models.Product:
    db_product = product_service.create(product)
    return db_product


@router.patch("/{product_id}", response_model=Product)
async def update_product(
    product_id: UUID4,
    product: ProductUpdate,
    product_service: ProductsService = Depends(get_products_service),
) -> Optional[models.Product]:
    return product_service.update(product_id, product)


@router.delete("/{product_id}", status_code=204)
async def delete_product(
    product_id: UUID4, product_service: ProductsService = Depends(get_products_service)
) -> Any:
    product_service.delete(product_id)
    return Response(status_code=204)
