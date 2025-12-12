from fastapi import FastAPI
from .config import create_config, Config
from app.presentation.controllers import main as routers
from app.presentation.exceptions import register_exception_handlers


def setup_routers(app: FastAPI) -> None:
    app.include_router(routers.router)


def create_application() -> FastAPI:
    config: Config = create_config()
    app: FastAPI = FastAPI(title=config.app.title, debug=config.app.debug)
    setup_routers(app)
    register_exception_handlers(app)
    return app


app = create_application()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main.main:app", host="0.0.0.0", port=8000, reload=True)