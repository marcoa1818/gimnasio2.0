from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config.db import Base


class users(Base):
    _tablename_ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255), index=True)
    password = Column(String(255), index=True)
    estatus = Column (Boolean, index=True)
  

       