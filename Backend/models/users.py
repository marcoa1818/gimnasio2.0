from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons
import enum 

class MyEstatus(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    bloqueado = "Bloqueado"
    Suspendido = "Suspendido"


class User(Base):
    __tablename__ = "tbb_usuarios"

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID= Column(Integer, ForeignKey("tbb_personas.ID"))
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(100))
    Contrasena = Column(LONGTEXT)
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column('value', Enum(MyEstatus))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    # Clave foranea para la relacion uno a uno con User