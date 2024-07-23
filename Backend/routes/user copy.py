from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user=APIRouter()
users=[]

#Users Model
class model_user(BaseModel):
    id: str
    usuario: str
    contrasena: str
    created_at: datetime = datetime.now()
    estatus:bool=False

@user.get("/")

def bienvenido():
    return "Bienvenido al sistema de API's"

@user.get('/users', tags=["Usuarios"])

def get_usuarios():
    return users

@user.post('/users', tags=["Usuarios"])
def save_usuarios(insert_users:model_user):
    users.append(insert_users)
    #print(insert_users)
    return "Datos guardados"

@user.put('/users/{user_id}', tags=["Usuarios"])
def update_usuario(user_id: str, updated_user:model_user):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "Datos actualizados"}
        
@user.delete('/users/{user_id}', tags=["Usuarios"])
def delete_usuario(user_id: str):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return {"message": "Usuario eliminado"}

