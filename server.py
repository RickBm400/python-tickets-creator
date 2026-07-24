from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }


@app.get("/greetins")
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
