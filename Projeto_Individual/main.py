from fastapi import Depends, FastAPI

#from .dependencies import get_query_token, get_token_header
#from .internal import admin
from .routers import userController # items, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(userController.router)
#app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}