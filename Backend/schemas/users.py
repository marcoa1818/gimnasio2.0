from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    Persona_Id: int
    Nombre_Usuario:str
    Contrasena:str
    Correo_Electronico:str
    Numero_Telefononico_Movil:str
    Estatus:str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    ID:int
    Persona_Id:int
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    Nombre_Usuario:str
    Correo_Electronico:str
    Contrasena:str
    Numero_Telefononico_Movil:str
        