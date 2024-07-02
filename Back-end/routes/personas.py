from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

persona = APIRouter()
personas = []

class Persona(BaseModel):
    id: str
    titulo_cortesia: str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    telefono: str
    correo: str
    genero : str
    fecha_nacimiento: datetime
    tipo_sangre : str
    created_at: datetime = datetime.now()
    estatus: bool = False

@persona.get("/")
def helloworld():
    return "Hola 9b idgs"

@persona.get("/personas",  tags=["Personas"])
def get_personas():
    return personas

@persona.post("/personas", tags=["Personas"])
def save_persona(insert_user: Persona):
    personas.append(insert_user)
    return {"message": "Datos guardados"}

@persona.put("/personas/{user_id}",  tags=["Personas"])
def Modificar_persona(user_id: str, updated_user: Persona):
    for index, user in enumerate(personas):
        if user.id == user_id:
            personas[index] = updated_user
            return {"message": "Usuario actualizado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@persona.delete("/personas/{user_id}",  tags=["Personas"])
def Eliminar_persona(user_id: str):
    for index, user in enumerate(personas):
        if user.id == user_id:
            del personas[index]
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@persona.get("/personas/{user_id}",  tags=["Personas"])
def Obtener_persona(user_id: str):
    for user in personas:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
