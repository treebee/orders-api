from typing import Any, List, Optional

from fastapi import Depends, Response
from fastapi.routing import APIRouter
from pydantic.types import UUID4

from orders_api.db import models
from orders_api.db.schemas import Store, StoreCreate, StoreUpdate
from orders_api.services import StoresService, get_stores_service

router = APIRouter(prefix="/stores")


@router.get("/", response_model=List[Store])
async def list_stores(
    store_service: StoresService = Depends(get_stores_service),
) -> List[models.Store]:
    return store_service.list()


@router.get(
    "/{store_id}",
    response_model=Store,
    responses={404: {"description": "Store not found"}},
)
async def get_store(
    store_id: UUID4, store_service: StoresService = Depends(get_stores_service)
) -> Optional[models.Store]:
    return store_service.get(store_id)


@router.post(
    "/",
    response_model=Store,
    status_code=201,
    responses={409: {"description": "Conflict Error"}},
)
async def create_store(
    store: StoreCreate, store_service: StoresService = Depends(get_stores_service)
) -> models.Store:
    return store_service.create(store)


@router.patch("/{store_id}", response_model=Store)
async def update_store(
    store_id: UUID4,
    store: StoreUpdate,
    store_service: StoresService = Depends(get_stores_service),
) -> Optional[models.Store]:
    return store_service.update(store_id, store)


@router.delete("/{store_id}", status_code=204)
async def delete_store(
    store_id: UUID4, store_service: StoresService = Depends(get_stores_service)
) -> Any:
    store_service.delete(store_id)
    return Response(status_code=204)
