from fastapi import APIRouter
from Projeto_Individual.models import userModel as User

router = APIRouter()

# Tag = aba qem que aparece na documentação do swagger
@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}


@router.post("/users/", tags=["users"])
async def create_user(user: User):
    return {"username": user.name}

#@router.delete("/users/", tags=["users"])