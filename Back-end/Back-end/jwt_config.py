from  jwt import encode, decode

def solicita_token (date:dict)-> str:
    token:str=encode(payload=dato,key='mi_clave', algorithm='h')