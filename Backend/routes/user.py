from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.users, config.db, schemas.users, models.users
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()
models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Ruta de bienvenida
@user.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

# Ruta para obtener todos los usuarios
@user.get('/users/', response_model=List[schemas.users.User],tags=['Usuarios'])
def read_users(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_users = crud.users.get_users(db=db,skip=skip, limit=limit)
    return db_users

# Ruta para obtener un usuario por ID
@user.post("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
def read_user(id: int, db: Session = Depends(get_db)):
    db_user= crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Ruta para crear un usurio
@user.post('/users/', response_model=schemas.users.User,tags=['Usuarios'])
def create_user(user: schemas.users.UserCreate, db: Session=Depends(get_db)):
    db_users = crud.users.get_user_by_usuario(db,usuario=user.Nombre_Usuario)
    if db_users:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.users.create_user(db=db, user=user)

# Ruta para actualizar un usuario
@user.put('/users/{id}', response_model=schemas.users.User,tags=['Usuarios'])
def update_user(id:int,user: schemas.users.UserUpdate, db: Session=Depends(get_db)):
    db_users = crud.users.update_user(db=db, id=id, user=user)
    if db_users is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo actualizar ")
    return db_users

# Ruta para eliminar un usuario
@user.delete('/users/{id}', response_model=schemas.users.User,tags=['Usuarios'])
def delete_user(id:int, db: Session=Depends(get_db)):
    db_users = crud.users.delete_user(db=db, id=id)
    if db_users is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar ")
    return db_users