from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    primer_apellido = Column(String(255))
    segundo_apellido= Column(String(255))
    direccion= Column(String(255))
    telefono= Column(String(255))
    correo= Column(String(255))
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)