import models.persons
import schemas.persons
from sqlalchemy.orm import Session
import models, schemas

def get_person(db: Session, id: int):
    return db.query(models.persons.Person).filter(models.persons.Person.id == id).first()

def get_person_by_persona(db: Session, nombre: str):
    return db.query(models.persons.Person).filter(models.persons.Person.nombre == nombre).first()

def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.persons.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.persons.PersonCreate):
    db_person = models.persons.Person(nombre=person.nombre, primer_apellido=person.primer_apellido, segundo_apellido=person.segundo_apellido, direccion=person.direccion, telefono=person.telefono, correo=person.correo, created_at=person.created_at, estatus=person.estatus)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def update_person(db: Session, id: int, person: schemas.persons.PersonUpdate):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.id == id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

def delete_person(db: Session, id: int):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.id == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person