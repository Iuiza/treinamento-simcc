# controller/producao_controller.py
from fastapi import APIRouter
from typing import List
from model.producao import Producoes
from controller.dao.producao_dao import listar_todos, listar_por_pesquisador

# Criação de um router chamado 'producao_router'
producao_router = APIRouter()

# Rota para listar todas as produções
@producao_router.get("/producoes", response_model=List[Producoes])
def listar():
    producoes = listar_todos()
    return producoes

# Rota para listar as produções de um determinado pesquisador
@producao_router.get("/pesquisadores/{pesquisadores_id}/producoes", response_model=List[Producoes])
def listar_por_pesquisador_route(pesquisadores_id: str):
    producoes = listar_por_pesquisador(pesquisadores_id)
    return producoes
