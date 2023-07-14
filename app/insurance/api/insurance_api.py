from fastapi import APIRouter
from fastapi import status

from insurance.models.insurance_model import InsuranceModel
from insurance.schemas.insurance_schemas import InsuranceCreate

insurance_router = APIRouter()


@insurance_router.post(
    '/create_insurance_type',
    tags=['Insurance'],
    status_code=201,
)
async def create_insurance(income: InsuranceCreate):
    for date, vals in income.dict().items():
        for val in vals:
            val['date'] = date
            await InsuranceModel.create(**val)
    return status.HTTP_201_CREATED


@insurance_router.get(
    '/get_all_insurance',
    tags=['Insurance'],
    status_code=200
)
async def get_all_insurance():
    query_result = await InsuranceModel.all()
    return query_result


@insurance_router.get(
    '/get_insurance_price',
    tags=['Insurance Value'],
    status_code=200,
)
async def get_insurance_price(
        case_date: str,
        cargo_type: str,
        declared_value: float) -> float:
    query_result = await InsuranceModel.filter(
                                                date=case_date,
                                                cargo_type=cargo_type).first()
    insurance_value = declared_value * float(query_result.rate)
    return insurance_value
