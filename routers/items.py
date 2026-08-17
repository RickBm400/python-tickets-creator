from typing import Optional
from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="",
    tags=["items"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/greetins")
def greetings(name: Optional[str] = None):
    try:
        if not name:
            raise ValueError("Not valid param")
        return {"message": "Hello " + name}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": "not creted", "code": "400"},
        ) from e
