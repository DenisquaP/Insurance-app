from fastapi import APIRouter
from insurance.api.insurance_api import insurance_router

router = APIRouter()
router.include_router(insurance_router)
