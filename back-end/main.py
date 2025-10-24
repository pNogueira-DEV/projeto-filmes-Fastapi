from fastapi import FastAPI
import funcao

#Como executar o fastapi
# python -m uvicorn main:app --reload

app= FastAPI(title='gerenciador de filmes')

@app.get("/")
def home():
    return ("mensagem de boas vindas")

@app.get("/filmes")
def criar_filme(titulo: str, genero: str, ano: int, nota: float):
    funcao.cadastrar_filme(titulo, genero, ano, nota)
    return {"mensagem": "Filme cadastrado com sucesso"}