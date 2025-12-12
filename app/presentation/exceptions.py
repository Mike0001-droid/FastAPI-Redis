from starlette import status
from app.domain import exception 
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(exception.ErrorInRedis)
    async def error_with_set_to_redis(_: Request, __: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Eror during writing to redis"},
        )