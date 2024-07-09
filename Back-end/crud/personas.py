import models.personas
import schemas.personas
from sqlalchemy.orm import Session
import models, schemas

def get_persona(db: Session, id: int):
    return db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()

def get_persona_by_id(db: Session, nombre: str):
    return db.query(models.personas.Persona).filter(models.personas.Persona.Nombre == nombre).first()

def get_personas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.personas.Persona).offset(skip).limit(limit).all()

def create_personas(db: Session, nom: schemas.personas.PersonaCreate):
    db_user = models.personas.Persona(Titulo_Cortesia=nom.Titulo_Cortesia,
                                      Nombre=nom.Nombre,
                                      Primer_Apellido=nom.Primer_Apellido, 
                                      Segundo_Apellido=nom.Segundo_Apellido,
                                      Fecha_Nacimiento=nom.Fecha_Nacimiento,  
                                      Fotografia=nom.Fotografia,  
                                      Genero=nom.Genero,  
                                      Tipo_Sangre=nom.Tipo_Sangre,  
                                      Estatus=nom.Estatus, 
                                      Fecha_Registro=nom.Fecha_Registro, 
                                      Fecha_Actualizacion=nom.Fecha_Actualizacion )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_personas(db: Session, id: int, person: schemas.personas.PersonaUpdate):
    db_user = db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()
    if db_user:
        for var, value in vars(person).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_personas(db: Session, id: int):
    db_user = db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user