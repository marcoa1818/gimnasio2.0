from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.roles import rol
from routes.usuarios_roles import userrol
# from routes.person import person
from routes.programas_saludables import programa_router  # Importa el router de Programas Saludables

app=FastAPI(
    title="Bull´s GYM",
    description="API para el almacenamiento de información de un gimnasio"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(programa_router, prefix="/api", tags=["Programas Saludables"])  # Agrega el router de Programas Saludables

print ("Hola bienvenido a mi backend")