import models.persons
import schemas.persons
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por ID
def get_person(db:Session, id: int):
    return db.query(models.persons.Person).filter(models.persons.Person.ID == id).first()

# Busqueda por nombre
def get_person_by_nombre(db:Session, nombre: str):
    return db.query(models.persons.Person).filter(models.persons.Person.Nombre == nombre).first()

# Buscar todos las personas
def get_persons(db:Session, skip: int=0, limit:int=10):
    return db.query(models.persons.Person).offset(skip).limit(limit).all()

# Crear una nueva personas
def create_person(db:Session, person: schemas.persons.PersonCreate):
    db_person = models.persons.Person(Titulo_Cortesia=person.Titulo_Cortesia,
                                    Nombre=person.Nombre,
                                    Primer_Apellido=person.Primer_Apellido,
                                    Segundo_Apellido=person.Segundo_Apellido,
                                    Fotografia=person.Fotografia,
                                    Genero=person.Genero,
                                    Tipo_Sangre=person.Tipo_Sangre,
                                    Fecha_Nacimiento=person.Fecha_Nacimiento,
                                    Fecha_Registro=person.Fecha_Registro,
                                    Fecha_Actualizacion=person.Fecha_Actualizacion,
                                    Estatus=person.Estatus)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# Actualizar una personas por ID
def update_person(db:Session, id:int, person:schemas.persons.PersonUpdate):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.ID == id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

# Eliminar una personas por ID
def delete_person(db:Session, id:int):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.ID == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person