from fastapi import APIRouter, HTTPException
from typing import Optional

router = APIRouter(
    prefix="",
    tags=["items"],
    dependencies=[],
    responses={ 404: { "description": "Not found" } }
)

@router.get("/")
async def root():
    return { "message": "Hello World" }


@router.get("/greetins")
def greetings(name: Optional[str] = None):
    try:
        if not name:
            raise ValueError("Not valid param")
        return {
            "message": "Hello " + name
        }
    except ValueError as error:
        print("Error: ", error)
        raise HTTPException(status_code=404, detail= {
            "message": str(error),
            "code": "400"
        })
