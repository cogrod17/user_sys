from fastapi import FastAPI
from v1.api import router as api_router
from fastapi_pagination import add_pagination


def init_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    add_pagination(app)
    return app


app = init_app()
