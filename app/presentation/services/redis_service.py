from typing import List
from app.domain import exception 
from redis import Redis, RedisError
from app.domain.entities import user
from fastapi import HTTPException, status


class RedisPhoneService:
    def __init__(self, redis_client: Redis):
        self.key_prefix = "phone:"
        self.redis_client = redis_client
    
    async def _get_user_data(self, phone: str) -> tuple[str, str]:
        key = self.key_prefix + phone
        address = await self.redis_client.get(key)
        if address is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with phone {phone} not found"
            )
        return key, address

    async def create(self, data: user.UserData) -> user.UserData:
        key = self.key_prefix + data.phone
        if await self.redis_client.exists(key):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
        try:
            await self.redis_client.setex(key, 2592000, data.address)
            return user.UserData.model_validate(data)
        except RedisError as e:
            raise exception.ErrorInRedis(str(e))
        
    async def get_all_users(self, limit: int = 100, offset: int = 0) -> List[user.UserData]:
        try:
            pattern = self.key_prefix + '*'
            all_keys = await self.redis_client.keys(pattern)
            start = offset
            end = offset + limit
            paginated_keys = all_keys[start:end]   
            results = []
            for key in paginated_keys:
                address = await self.redis_client.get(key)
                if address:
                    phone_key = key.decode('utf-8') if isinstance(key, bytes) else key
                    phone = phone_key.replace(self.key_prefix, '')
                    results.append({
                        "phone": phone,
                        "address": address.decode('utf-8') if isinstance(address, bytes) else address
                    })
            return results
        
        except RedisError as e:
            raise exception.ErrorInRedis(str(e))
        
    async def get_by_phone(self, phone: str) -> user.UserData:
        try:
            key, address = await self._get_user_data(phone)
            address_str = address.decode('utf-8') if isinstance(address, bytes) else address
            user_data = {"phone": phone, "address": address_str}
            return user.UserData.model_validate(user_data)
        except RedisError as e:
            raise exception.ErrorInRedis(str(e))
        
    async def update_address(self, data: user.UserData) -> user.UserData:
        try:
            key, _ = await self._get_user_data(data.phone)
            ttl = await self.redis_client.ttl(key)
            if ttl > 0:
                await self.redis_client.setex(key, ttl, data.address)
            else:
                await self.redis_client.set(key, data.address)
            return user.UserData(phone=data.phone, address=data.address) 
        except RedisError as e:
            raise exception.ErrorInRedis(str(e))
        
    async def delete(self, phone: str) -> bool:
        try:
            key, _ = await self._get_user_data(phone)
            deleted_count = await self.redis_client.delete(key)
            return deleted_count > 0
        except RedisError as e:
            raise exception.ErrorInRedis(str(e))

