from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = []

#usersModel
class model_user(BaseModel):
    id:str
    usuario:str
    contrasena:str
    created_at:datetime = datetime.now
    estatus:bool=False
    
    
@user.get("/")

def bienvenido():
    return "Bienvenido al sistema de apis"

@user.get("/users")

def get_usuarios():
    return users

@user.post('/users')

def save_usuarios(users:model_user):
    users.append
    return "Datos Guardados"
