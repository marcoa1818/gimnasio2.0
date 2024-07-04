from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class PersonBase(BaseModel):
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    telefono: str
    correo: str
    created_at: datetime
    estatus: bool

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True