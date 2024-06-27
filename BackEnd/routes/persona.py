from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

persona = APIRouter()
personas = []

class model_persona(BaseModel):
    id: str
    titulo_cortesia: str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    fecha_nacimiento: str
    fotografia: str
    contraseña: str
    genero: str
    tipo_sangre: str
    create_at: datetime = datetime.now()
    estatus: bool = False

@persona.get("/")

@persona.get("/Personas", tags=["Personas"])
def get_personas():
    return personas

@persona.post("/persona", response_model=List[model_persona],tags=["Personas"])
def get_personas(id: Optional[str] = Query(None, description="ID de la persona a buscar")):
    if id:
        filtered_personas = [persona for persona in personas if persona.id == id]
        if not filtered_personas:
            raise HTTPException(status_code=404, detail="User not found")
        return filtered_personas
    return personas

# Método POST
@persona.post("/personas", response_model=model_persona, tags=["Personas"])
def save_personas(insert_personas: model_persona):
    personas.append(insert_personas)
    print(insert_personas)
    return insert_personas

# Método PUT
@persona.put("/edit_persona", response_model=model_persona, tags=["Personas"])
def update_persona(persona_id: str, updated_persona: model_persona):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas[index] = updated_persona
            return updated_persona
    raise HTTPException(status_code=404, detail="User not found")

# Método DELETE
@persona.delete("/delete_persona", tags=["Personas"])
def delete_persona(persona_id: str):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[index]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
