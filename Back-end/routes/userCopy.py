from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = []

class User(BaseModel):
    id: str
    usuario: str
    contrasena: str
    created_at: datetime = datetime.now()
    estatus: bool = False

@user.get("/", )
def helloworld():
    return "Hola 9b idgs"

@user.get("/users",tags=["Usuarios"] )
def get_users():
    return users

@user.post("/users", tags=["Usuarios"])

def save_user(insert_user: User, ):
    users.append(insert_user)
    return {"message": "Datos guardados"}

@user.put("/users/{user_id}", tags=["Usuarios"])
def Modificar_usuario(user_id: str, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "Usuario actualizado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.delete("/users/{user_id}", tags=["Usuarios"])
def Eliminar_usuario(user_id: str):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@user.get("/users/{user_id}", tags=["Usuarios"])
def Obtener_usuario(user_id: str):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
