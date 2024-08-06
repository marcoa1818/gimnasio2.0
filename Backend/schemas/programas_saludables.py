from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstatusPrograma(str, Enum):
    Registrado = "Registrado"
    Sugerido = "Sugerido"
    Aprobado_Medico = "Aprobado por el Médico"
    Aprobado_Usuario = "Aprobado por el Usuario"
    Rechazado_Medico = "Rechazado por el Médico"
    Rechazado_Usuario = "Rechazado por el Usuario"
    Terminado = "Terminado"
    Suspendido = "Suspendido"
    Cancelado = "Cancelado"

class ProgramaBase(BaseModel):
    Nombre: str
    Usuario_ID: int
    Instructor_ID: int
    Fecha_Creacion: datetime
    Estatus: EstatusPrograma
    Duracion: str
    Porcentaje_Avance: float
    Fecha_Ultima_Actualizacion: Optional[datetime] = None

class ProgramaCreate(ProgramaBase):
    pass

class ProgramaUpdate(ProgramaBase):
    pass

class Programa(ProgramaBase):
    ID: int
    class Config:
        orm_mode = True