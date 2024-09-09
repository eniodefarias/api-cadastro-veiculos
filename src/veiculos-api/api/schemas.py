from pydantic import BaseModel
from typing import Optional
from enum import Enum

# Enum para status do veículo
class VeiculoStatus(str, Enum):
    CONECTADO = "CONECTADO"
    DESCONECTADO = "DESCONECTADO"

# Modelo de resposta com ID para Veículo
class VeiculoResponse(BaseModel):
    id: int
    placa: str
    marca: str
    modelo: str
    cor: str
    status: VeiculoStatus

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str
