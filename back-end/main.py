from fastapi import FastAPI
import funcao

#Como executar o fastapi
# python -m uvicorn main:app --reload

app= FastAPI(title='gerenciador de filmes')

@app.get("/")
def home():
    return ("mensagem: Bem vindo ao gerenciador de filmes")

@app.post("/filme")
def criar_filme(titulo: str, genero: str, ano: int, nota: float):
    funcao.cadastrar_filme(titulo, genero, ano, nota)
    return {"mensagem": "Filme cadastrado com sucesso"}




@app.get("/filme")
def listar_filmes():
    filmes = funcao.listar_filmes()
    lista = []
    for linha in filmes:
        lista.append(
            {
                "id": linha[0],
                "titulo": linha[1],
                "genero": linha[2],
                "ano": linha[3],
                "nota": linha[4]
            }
        )
    return {"filmes": lista}



@app.delete("/filme/{id_filme}")
def deletar_filmes(id_filme:int):
    filmes = funcao.buscar_filme(id_filme)
    if filmes:
        funcao.deletar_filmes(id_filme)
        return {"mensagem": "Filme deletado com sucesso"}
    else:
        return {"mensagem": "Filme não encontrado"}
    

@app.put("/filme/{id_filme}")
def atualizar_filme(id: int, nova_nota: float ):
    filmes = funcao.buscar_filme(id)
    if filmes:
        funcao.atualizar_nota(id, nova_nota)
        return{"mensagem": "Filme atualizado com sucesso!"}
    else:
        return{"erro": "Filme não encontrado"}

    

