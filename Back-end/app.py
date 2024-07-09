from fastapi import FastAPI
from routes.user import user
from routes.personas import persona
from routes.roles import rol


app=FastAPI()
app.include_router(user)
app.include_router(persona)
app.include_router(rol)
print("Hola bienvenido a mi backend")