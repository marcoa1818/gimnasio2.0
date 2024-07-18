import models.roles
import models.usuarios_roles
import schemas.usuarios_roles
from sqlalchemy.orm import Session
import models, schemas

def get_userrol_by_ids(db: Session, usuario_id: int, rol_id: int):
    return db.query(models.usuarios_roles.Usuario_Rol).filter(
        models.usuarios_roles.Usuario_Rol.Usuario_ID == usuario_id,
        models.usuarios_roles.Usuario_Rol.Rol_ID == rol_id
    ).first()
def get_usuario_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.usuarios_roles.Usuario_Rol).offset(skip).limit(limit).all()

def create_usuario_rol(db: Session, usuario_rol: schemas.usuarios_roles.Usuario_RolCreate):
    db_user = models.usuarios_roles.Usuario_Rol(
                                Usuario_ID = usuario_rol.Usuario_ID,
                                Rol_ID = usuario_rol.Rol_ID,
                                Estatus=usuario_rol.Estatus, 
                                Fecha_Registro=usuario_rol.Fecha_Registro,
                                Fecha_Actualizacion=usuario_rol.Fecha_Actualizacion
                                )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_userrol(db: Session, usuario_id: int, rol_id: int, userrol: schemas.usuarios_roles.Usuario_RolUpdate):
    db_userrol = db.query(models.usuarios_roles.Usuario_Rol).filter(
        models.usuarios_roles.Usuario_Rol.Usuario_ID == usuario_id,
        models.usuarios_roles.Usuario_Rol.Rol_ID == rol_id
    ).first()
    if db_userrol:
        # Actualiza solo los campos deseados
        db_userrol.Estatus = userrol.Estatus
        db_userrol.Fecha_Registro = userrol.Fecha_Registro
        db_userrol.Fecha_Actualizacion = userrol.Fecha_Actualizacion

        db.commit()
        db.refresh(db_userrol)
    return db_userrol

def delete_usuario_rol(db: Session, id_user: int, id_rol: int):
    db_user_rol = db.query(models.usuarios_roles.Usuario_Rol).filter(
                                models.usuarios_roles.Usuario_Rol.Usuario_ID == id_user, models.usuarios_roles.Usuario_Rol.Rol_ID == id_rol).first()
    if db_user_rol:
        db.delete(db_user_rol)
        db.commit()
    return db_user_rol