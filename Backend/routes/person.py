from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.persons, config.db, schemas.persons, models.persons
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

person = APIRouter()

models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@person.get("/persons/", response_model=List[schemas.persons.Person], tags=["Personas"])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persons= crud.persons.get_persons(db=db, skip=skip, limit=limit)
    return db_persons

@person.post("/person/{id}", response_model=schemas.persons.Person, tags=["Personas"])
def read_persons(id: int, db: Session = Depends(get_db)):
    db_person= crud.persons.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@person.post("/persons/", response_model=schemas.persons.Person, tags=["Personas"])
def create_person(person: schemas.persons.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person_by_persona(db, nombre=person.nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.persons.create_person(db=db, person=person)

@person.put("/person/{id}", response_model=schemas.persons.Person, tags=["Personas"])
def update_person(id: int, person: schemas.persons.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.persons.update_person(db=db, id=id, person=person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizado")
    return db_person

@person.delete("/person/{id}", response_model=schemas.persons.Person, tags=["Personas"])
def delete_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.persons.delete_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_person






# from fastapi import APIRouter
# from pydantic import BaseModel
# from datetime import datetime

# person = APIRouter()
# persons = [

# ]
# class models_person(BaseModel):
#     id:str
#     nombre:str
#     primer_apellido: str
#     segundo_apellido: str
#     direccion: str
#     telefono:str
#     correo: str
#     sangre: str
#     fecha_nacimiento: datetime
#     created_at:datetime = datetime.now()
#     estatus:bool=False

# @person.get("/")

# def bienvenido():
#     return "Hola 9B"

# @person.get("/person", tags=['Personas'])

# def getPerson():
#     return persons

# @person.post("/person/{person_id}", tags=['Personas'])

# def postPerson(person_id: str):
#     for person in persons:
#         if person.id == person_id:
#             return person

# @person.post('/person', tags=['Personas'])

# def insertPerson(insert_person:models_person):
#     persons.append(insert_person)
#     return {"message": f"Se ha insertado un nuevo usuario con el ID: {insert_person.id}"}

# @person.put('/person/{person_id}', tags=['Personas'])

# def updatePerson(update_person:models_person, person_id: str):
#     print(update_person)
#     for index, person in enumerate(persons):
#         if person.id == person_id:
#             update_person.created_at = person.created_at
        
#             persons[index] = update_person
            
#             return {"message": f"Se ha modificado correctamente a la persona con el ID: {person_id}"}

# @person.delete('/person/{person_id}', tags=['Personas'])

# def deletePerson(person_id: str):
#     for index, person in enumerate(persons):
#         if person.id == person_id:
#             persons.pop(index)
#             return {"message": f"Se ha eliminado correctamente a la persona con el ID: {person_id}"}

