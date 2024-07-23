from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Date
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base


class Rol(Base):
    __tablename__ = "tbc_roles"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(80))
    Descripcion = Column(LONGTEXT)
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)