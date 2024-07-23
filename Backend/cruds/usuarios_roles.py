import models.usuarios_roles
import schemas.usuarios_roles
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por usuario_id y rol_id
def get_userrol_by_ids(db: Session, usuario_id: int, rol_id: int):
    return db.query(models.usuarios_roles.UserRol).filter(
        models.usuarios_roles.UserRol.Usuario_ID == usuario_id,
        models.usuarios_roles.UserRol.Rol_ID == rol_id
    ).first()

# Buscar todos los usuaurios-roless
def get_usersrols(db:Session, skip: int=0, limit:int=10):
    return db.query(models.usuarios_roles.UserRol).offset(skip).limit(limit).all()

# Crear nuevo usuaurios-roles
def create_userrol(db:Session, userrol: schemas.usuarios_roles.UserRolCreate):
    db_userrol = models.usuarios_roles.UserRol(Usuario_ID=userrol.Usuario_ID, 
                                          Rol_ID=userrol.Rol_ID,
                                          Estatus=userrol.Estatus, 
                                          Fecha_Registro=userrol.Fecha_Registro, 
                                          Fecha_Actualizacion=userrol.Fecha_Actualizacion)
    db.add(db_userrol)
    db.commit()
    db.refresh(db_userrol)
    return db_userrol

# Actualizar un usuario-rol
def update_userrol(db: Session, usuario_id: int, rol_id: int, userrol: schemas.usuarios_roles.UserRolUpdate):
    db_userrol = db.query(models.usuarios_roles.UserRol).filter(
        models.usuarios_roles.UserRol.Usuario_ID == usuario_id,
        models.usuarios_roles.UserRol.Rol_ID == rol_id
    ).first()
    if db_userrol:
        # Actualiza solo los campos deseados
        db_userrol.Estatus = userrol.Estatus
        db_userrol.Fecha_Registro = userrol.Fecha_Registro
        db_userrol.Fecha_Actualizacion = userrol.Fecha_Actualizacion

        db.commit()
        db.refresh(db_userrol)
    return db_userrol

# Eliminar un usuaurios-roles por id
def delete_userrol(db:Session,  usuario_id: int, rol_id: int):
    db_userrol = db.query(models.usersrols.UserRol).filter(models.usersrols.UserRol.Usuario_ID == usuario_id,
                                                           models.usersrols.UserRol.Rol_ID == rol_id
    ).first()
    if db_userrol:
        db.delete(db_userrol)
        db.commit()
    return db_userrol