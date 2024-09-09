from sqlalchemy.orm import Session
from .models import User, pwd_context
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException

SECRET_KEY = "passwd"  # Substitua pela sua chave secreta
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and user.verify_password(password):
        return user
    return None

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar o token JWT
# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload.get("user_id")
#     except JWTError:
#         return None

# Função para decodificar e verificar o token
# def verify_token(token: str):
#     print(f"verify_token token: {token}")
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         print(f"verify_token payload: {payload}")
#         user_id = payload.get("sub")
#         if user_id is None:
#             return None
#         return user_id
#     except JWTError:
#         print(f"verify_token JWTError: {JWTError}")
#         print(f"verify_token inválido: {token}")
#         return None



def verify_token(token: str):
    try:
        print(f"verify_token token: {token}")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"verify_token payload: {payload}")
        return payload.get("sub")  # Retorna o usuário se o token for válido
    except JWTError:
        return None


# Função para criar novos usuários
def create_user(db: Session, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
