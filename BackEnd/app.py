from fastapi import FastAPI
from routes.user import user
from routes.persona import persona 

app=FastAPI()
app.include_router(user)
app.include_router(persona)
print("Hola bienvenido")