# pip install streamlit requests
import streamlit as st
import requests

#URL da API FastAPI

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Filmes", layout="wide")
st.title("Gerenciador de Filmes")

menu = st.sidebar.radio ("Menu", 
                         ["Cadastrar filmes", "Listar filmes", "Deletar filmes"]
                         )

if menu == "Listar filmes":
    st.subheader("Todos os filmes disponiveis: ")
    response = requests.get(f"{API_URL}/filme")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if  filmes:
            st.dataframe(filmes)
        else:
            st.write("Nenhum filme cadastrado.")

    else:
        st.write("Não foi possivel exibir os filmes")


elif menu == "Cadastrar filmes":
    st.subheader("➕ Adicionar novos filmes")
    titulo = st.text_input("Titulo do filme")
    genero = st.text_input("Genero do filme")
    ano = st.number_input("Ano de lançamento", min_value=1900, max_value=2100, step=1)
    nota = st.number_input("Nota (0 a 10)", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Salvar filme"):
        dados = {"titulo": titulo, "genero": genero, "ano": ano, "nota": nota}
        response = requests.post(f"{API_URL}/filme", params=dados)
        if response.status_code == 200:
            st.success("Filme cadastrado com sucesso!")
        else:
            st.error("Erro ao cadastrar o filme.")

elif menu == "Deletar filmes":
    st.subheader("🗑️ Deletar filmes")
    id_filme = st.number_input("id do filme a ser deletado", min_value=1, step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/filme/{id_filme}")
        if response.status_code == 200:
            data = response.json()
            if "error" not in data:
                st.success("Filme excluído com sucesso!")
            else:
                st.error("Erro ao tentar excluir o filme")
        else:
            st.error("Erro ao excluir o filme")



        
