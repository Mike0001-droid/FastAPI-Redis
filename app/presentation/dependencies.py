from typing import Annotated
from functools import lru_cache
from fastapi import Depends, Query
from .services import redis_service
from pydantic import BaseModel, Field
from app.domain.entities import phone
from app.main.redis import redis_client



class Pagination(BaseModel):
    limit: int = Field(5, ge=0, lt=100, description="Кол-во элементов на странице")
    offset: int = Field(5, ge=0, description="Смещение для пагинации")


@lru_cache
def get_redis_phone_service() -> redis_service.RedisPhoneService:
    return redis_service.RedisPhoneService(redis_client)

def validate_phone_number(phone_str: str = Query(...)) -> phone.PhoneModel:
    return phone.PhoneModel(phone=phone_str)


PhoneDep = Annotated[phone.PhoneModel, Depends(validate_phone_number)]
PaginationDep = Annotated[Pagination, Depends(Pagination)]
RedisServiceDep = Annotated[redis_service.RedisPhoneService, Depends(get_redis_phone_service)]
