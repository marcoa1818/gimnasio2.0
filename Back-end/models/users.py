from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum
import models.personas

class User(Base):
    __tablename__ = "tbb_users"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255))
    password = Column(LONGTEXT)
    estatus = Column(Boolean, default=False)
    Id_persona = Column(Integer)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    #items = relationship("Item", back_populates="owner") Clave Foranea




