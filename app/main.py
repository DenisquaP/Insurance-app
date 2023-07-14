from fastapi import FastAPI
from insurance.router import router

from tortoise.contrib.fastapi import register_tortoise

from settings import settings

app = FastAPI()

app.include_router(router)

register_tortoise(
    app,
    db_url=settings.database_url,
    modules={"models": ["insurance.models.insurance_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
