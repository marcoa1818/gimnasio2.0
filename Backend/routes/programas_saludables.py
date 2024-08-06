from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import cruds.programas_saludables, config.db, schemas.programas_saludables, models.programas_saludables
from typing import List
from portadortoken import Portador

programa_router = APIRouter()

models.programas_saludables.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@programa_router.get("/programas_saludables/", response_model=List[schemas.programas_saludables.Programa], tags=["Programas Saludables"])
def read_programas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_programas = cruds.programas_saludables.get_programas(db=db, skip=skip, limit=limit)
    return db_programas

@programa_router.get("/programa/{id}", response_model=schemas.programas_saludables.Programa, tags=["Programas Saludables"])
def read_programa(id: int, db: Session = Depends(get_db)):
    db_programa = cruds.programas_saludables.get_programa(db=db, id=id)
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return db_programa

@programa_router.post("/programas_saludables/", response_model=schemas.programas_saludables.Programa, tags=["Programas Saludables"])
def create_programa(programa: schemas.programas_saludables.ProgramaCreate, db: Session = Depends(get_db)):
    return cruds.programas_saludables.create_programa(db=db, programa=programa)

@programa_router.put("/programa/{id}", response_model=schemas.programas_saludables.Programa, tags=["Programas Saludables"])
def update_programa(id: int, programa: schemas.programas_saludables.ProgramaUpdate, db: Session = Depends(get_db)):
    db_programa = cruds.programas_saludables.update_programa(db=db, id=id, programa=programa)
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return db_programa

@programa_router.delete("/programa/{id}", response_model=schemas.programas_saludables.Programa, tags=["Programas Saludables"])
def delete_programa(id: int, db: Session = Depends(get_db)):
    db_programa = cruds.programas_saludables.delete_programa(db=db, id=id)
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return db_programa
