from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"Hola": "Juan"}


class User(BaseModel):
    userName: str
    email: str
    password: str


@app.post("/users/")
async def create_user(user: User):
    return {
        "username": user.userName,
        "Email": user.email,
        "Password": hash(user.password)
    }


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {
        "user_id": user_id,
        "username": user.userName,
        "email": user.email,
        "Password": hash(user.password)
    }


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {
        "message": f"Usuario con el"
                   f" id: {user_id} eliminado"
                   f" correctamente"
    }


class UserUpdate(BaseModel):
    email: Optional[str] = None


@app.patch("/users/{user_id}")
async def partial_update_user(user_id: int, user_update: UserUpdate):
    return {
        "user_id": user_id,
        "email:": user_update.email
    }


datos_ejemplos = {
    1: {"nombre": "ejemplo 1", "descripcion": "descripcion 1"},
    2: {"nombre": "ejemplo 2", "descripcion": "descripcion 2"},
    3: {"nombre": "aceite", "descripcion": "descripcion"},
    4: {"nombre": "aceite 2", "descripcion": "descripcion"},
}


@app.get("/datos/{id}")
def obtener_datos(id: int):
    return (datos_ejemplos
            .get(id, {"error": "no se encontraron datos con ese id"}))
