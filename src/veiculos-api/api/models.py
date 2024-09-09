from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from passlib.context import CryptContext
import enum

SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Modelo do usuário
# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)

#     def verify_password(self, password: str):
#         return pwd_context.verify(password, self.hashed_password)

# Enum para status do veículo
class VeiculoStatus(str, enum.Enum):
    CONECTADO = "CONECTADO"
    DESCONECTADO = "DESCONECTADO"

# Modelo do usuário
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.hashed_password)

# Modelo do veículo
class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    cor = Column(String)
    status = Column(Enum(VeiculoStatus), default=VeiculoStatus.DESCONECTADO)



# Função para criar o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Criação das tabelas no banco de dados
# def init_db():
#     Base.metadata.create_all(bind=engine)