from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Veiculo, VeiculoStatus, get_db
from pydantic import BaseModel
from typing import List
from .schemas import VeiculoResponse

router = APIRouter()

# Pydantic model para criação de veículo
class VeiculoCreate(BaseModel):
    placa: str
    marca: str
    modelo: str
    cor: str
    status: VeiculoStatus = VeiculoStatus.DESCONECTADO  # Valor padrão

# exmplo: curl -X 'GET' 'http://127.0.0.1:8000/veiculos'  -H 'accept: application/json'  -H 'Authorization: Bearer <token>'

# GET /veiculos: Retorna a lista de veículos
@router.get("/veiculos", response_model=List[VeiculoResponse])
def listar_veiculos(db: Session = Depends(get_db)):
    print(f"listar_veiculos db: {db}")
    veiculos = db.query(Veiculo).all()
    print(f"listar_veiculos veiculos1: {db.query(Veiculo)}")
    print(f"listar_veiculos veiculos2: {veiculos}")
    return veiculos

# POST /veiculos: Cria um novo veículo
@router.post("/veiculos", response_model=VeiculoCreate)
def criar_veiculo(veiculo: VeiculoCreate, db: Session = Depends(get_db)):
    db_veiculo = Veiculo(
        placa=veiculo.placa,
        marca=veiculo.marca,
        modelo=veiculo.modelo,
        cor=veiculo.cor,
        status=veiculo.status
    )
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

# GET /veiculos/{id}: Retorna os detalhes de um veículo específico
@router.get("/veiculos/{id}", response_model=VeiculoCreate)
def obter_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id == id).first()
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo

# PUT /veiculos/{id}: Atualiza o status de um veículo
@router.put("/veiculos/{id}")
def atualizar_status_veiculo(id: int, status: VeiculoStatus, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id == id).first()
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    veiculo.status = status
    db.commit()
    db.refresh(veiculo)
    return {"message": "Status atualizado com sucesso", "veiculo": veiculo}

# DELETE /veiculos/{id}: Exclui um veículo
@router.delete("/veiculos/{id}")
def excluir_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id == id).first()
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    db.delete(veiculo)
    db.commit()
    return {"message": "Veículo excluído com sucesso"}
