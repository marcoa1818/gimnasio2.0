from fastapi import HTTPException, Request, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from jwt_config import valida_token
import cruds.users, config.db, models.users

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Portador(HTTPBearer):
    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        autorizacion = await super().__call__(request)
        dato = valida_token(autorizacion.credentials)
        db_userlogin = cruds.users.get_user_by_credentials(db, username=dato["Nombre_Usuario"],
                                                           correo=dato["Correo_Electronico"],
                                                           telefono=dato["Numero_Telefono"],
                                                           password=dato["Contrasena"])
        if db_userlogin is None:
            raise HTTPException(status_code=404, detail="Login Incorrrecto")
        return db_userlogin