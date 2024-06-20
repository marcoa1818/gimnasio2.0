from fastapi import APIRouter
user = APIRouter()

@user.get("/user")

def hellowordId():
    return "Holaaaa"