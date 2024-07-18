from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from typing import List

key = Fernet.generate_key()
f = Fernet(key)
usuario_rol = APIRouter()
models.usuarios_roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Rols
@usuario_rol.get('/usersrols/', response_model=List[schemas.usuarios_roles.Usuario_Rol],tags=['Usuarios-Roles'])
def read_rols(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_userrols = crud.usuarios_roles.get_usuario_roles(db=db,skip=skip, limit=limit)
    return db_userrols

# Ruta para obtener un usuariorol por usuario ID
@usuario_rol.post("/usersrol/{usuario_id}/{rol_id}", response_model=schemas.usuarios_roles.Usuario_Rol, tags=["Usuarios-Roles"])
def get_userrol_by_ids(usuario_id: int, rol_id: int, db: Session = Depends(get_db)):
    db_userrol = crud.usuarios_roles.get_userrol_by_ids(db=db, usuario_id=usuario_id, rol_id=rol_id)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="User-Rol not found")
    return db_userrol

# Ruta para crear un usuario-rol
@usuario_rol.post('/usersrols/', response_model=schemas.usuarios_roles.Usuario_Rol,tags=['Usuarios-Roles'])
def create_rol(userrol: schemas.usuarios_roles.Usuario_RolCreate, db: Session=Depends(get_db)):
    db_userrols = crud.usuarios_roles.get_userrol_by_ids(db, usuario_id=userrol.Usuario_ID, rol_id=userrol.Rol_ID)
    if db_userrols:
        raise HTTPException(status_code=400, detail="User-Rol existente intenta nuevamente")
    return crud.usuarios_roles.create_usuario_rol(db=db, usuario_rol=userrol)

# Ruta para actualizar un usuario-rol
@usuario_rol.put("/usersrol/{usuario_id}/{rol_id}", response_model=schemas.usuarios_roles.Usuario_Rol, tags=["Usuarios-Roles"])
def update_userrol(usuario_id: int, rol_id: int, userrol:schemas.usuarios_roles.Usuario_RolUpdate, db: Session = Depends(get_db)):
    db_userrol = crud.usuarios_roles.update_userrol(db=db, usuario_id=usuario_id, rol_id=rol_id, userrol=userrol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="User-Rol not found")
    return db_userrol

# Ruta para eliminar un Rol
@usuario_rol.delete('/usersrols/{usuario_id}/{rol_id}', response_model=schemas.usuarios_roles.Usuario_Rol,tags=['Usuarios-Roles'])
def delete_rol(usuario_id: int, rol_id: int, db: Session=Depends(get_db)):
    db_userrols = crud.usuarios_roles.delete_usuario_rol(db=db, usuario_id=usuario_id,rol_id=rol_id )
    if db_userrols is None:
        raise HTTPException(status_code=404, detail="User-Rol no existe, no se pudo eliminar ")
    return db_userrols