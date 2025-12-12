from fastapi import APIRouter
from app.domain.entities import user
from app.presentation.dependencies import RedisServiceDep, \
    PaginationDep, PhoneDep


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/users")
async def create_user(
    user: user.UserData,
    service: RedisServiceDep
):
    return await service.create(user)

@router.get("/users")
async def get_all(
    pagination: PaginationDep,
    service: RedisServiceDep,
):
    return await service.get_all_users(
        pagination.limit,
        pagination.offset
    )

@router.get("/user")
async def get(
    phone_data: PhoneDep,
    service: RedisServiceDep,
):
    return await service.get_by_phone(phone_data.phone)

@router.put("/user")
async def update(
    user: user.UserData,
    service: RedisServiceDep,
):
    return await service.update_address(user)

@router.delete("/user")
async def delete(
    phone_data: PhoneDep,
    service: RedisServiceDep,
):
    return await service.delete(phone_data.phone)