from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter

from orders_api.services import StoresService, get_stores_service
from orders_api.db.schemas import Store, StoreCreate


router = APIRouter(prefix="/stores")


@router.get("/", response_model=List[Store])
async def list_stores(store_service: StoresService = Depends(get_stores_service)):
    return store_service.list()


@router.get("/{store_id}", response_model=Store)
async def get_store(
    store_id: int, store_service: StoresService = Depends(get_stores_service)
):
    return store_service.get(store_id)


@router.post("/", response_model=Store, status_code=201)
async def create_store(
    store: StoreCreate, store_service: StoresService = Depends(get_stores_service)
):
    return store_service.create(store)