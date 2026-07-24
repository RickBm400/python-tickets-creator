from fastapi import APIRouter

router = APIRouter(
    prefix="/metrics",
    tags=["metrics"],
    dependencies=[],
    responses={ 404: { "description": "Not found" } }
)

@router.get("")
def read_metrics():
    return {
        "details": "metrics created"
    }