from fastapi import APIRouter, Depends
from config.db import SessionLocal, engine
import schemas, models
from cruds import crud
from sqlalchemy.orm import Session


user = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user.get("/")

def bienvenido():
    return "Bienvenido al sistema de API's"

@user.get('/users', response_model=list[schemas.users], tags=["Usuarios"])

def get_usuarios(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# @user.post('/users', tags=["Usuarios"])
# def save_usuarios(insert_users:model_user):
#     users.append(insert_users)
#     #print(insert_users)
#     return "Datos guardados"

# @user.put('/users/{user_id}', tags=["Usuarios"])
# def update_usuario(user_id: str, updated_user:model_user):
#     for index, user in enumerate(users):
#         if user.id == user_id:
#             users[index] = updated_user
#             return {"message": "Datos actualizados"}
        
# @user.delete('/users/{user_id}', tags=["Usuarios"])
# def delete_usuario(user_id: str):
#     for index, user in enumerate(users):
#         if user.id == user_id:
#             del users[index]
#             return {"message": "Usuario eliminado"}