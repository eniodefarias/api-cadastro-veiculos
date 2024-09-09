from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .models import Base, engine, get_db, User
from .auth import authenticate_user, create_access_token, create_user, verify_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from .schemas import UserCreate  # Importe o modelo UserCreate
import uvicorn
from .init_db import init_db  # Importe a função de inicialização
from typing import Optional
from .veiculos import router as veiculos_router

app = FastAPI(
    title="veiculos-api",
    description="API Restful para cadastros de veículos e autenticação",
    version="0.0.1",
)

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)
init_db()  # Chame a função de inicialização

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(veiculos_router)

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    print(f"register: user: {user}")    
    print(f"register: db: {db}")    
    print(f"register: token: {token}")    
    user_id = verify_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token or token expired")
    create_user(db, user.username, user.password)
    return {"message": f"Usuário \"{user.username}\" criado com sucesso"}

# @app.get("/protected")
# def protected_route(Authorization: str = Header(...), db: Session = Depends(get_db)):
#     print(f"protected_route Authorization: {Authorization}")
#     print(f"protected_route db: {db}")
#     token = Authorization.split(" ")[1]  # Extrai o token do cabeçalho
#     print(f"protected_route token: {token}")
#     user_id = verify_token(token)
#     print(f"protected_route user_id: {user_id}")
#     if user_id:
#         return {"message": "Access granted", "user_id": user_id}
#     else:
#         raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/protected")
def protected_route(
    Authorization: Optional[str] = Header(),  # Define Authorization como opcional
    db: Session = Depends(get_db)
):
    # exmplo: curl -X 'GET' 'http://127.0.0.1:8000/protected'  -H 'accept: application/json'  -H 'Authorization: Bearer <token>'
    # Authorization deve ser informado assim:    Bearer <token>
    print(f"protected_route ")
    print(f"protected_route Authorization: {Authorization}")

    print(f"protected_route db: {db}")
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    if "Bearer " not in Authorization:
        raise HTTPException(status_code=401, detail="Invalid Authorization header format. use Bearer <token>")
        
    token = Authorization.split(" ")[1]  # Extrai o token do cabeçalho
    print(f"protected_route token: {token}")
    user_id = verify_token(token)  # Certifique-se de que você tem a função verify_token
    print(f"protected_route user_id: {user_id}")
    if user_id:
        return {"message": "Access granted", "user_id": user_id}
    else:
        print(f"protected_route Unauthorized: {Authorization}")
        raise HTTPException(status_code=401, detail="Unauthorized")



@app.get("/healthcheck")
def read_healthcheck():
    return {"status": "WORKING"}

# if __name__ == "__main__":
#     uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
