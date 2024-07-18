from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum
from sqlalchemy import PrimaryKeyConstraint


class Usuario_Rol(Base):
    __tablename__ = "tbd_usuarios_roles"

    Usuario_ID = Column(Integer, ForeignKey("tbb_users.ID"))
    Rol_ID = Column(Integer, ForeignKey("tbc_roles.ID"))
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner") Clave Foranea


    __table_args__ = (
        PrimaryKeyConstraint('Usuario_ID', 'Rol_ID'),
    )