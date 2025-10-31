# pip install streamlit requests
import streamlit as st
import requests

#URL da API FastAPI

API_URL = "http://127.0.0.1:8000"

st.title("Gerenciador de Filmes")

menu = st.sidebar.radio ("Menu", 
                         ["Cadastrar filmes", "Listar filme"]
                         )

if menu == "Listar filme":
    st.subheader("Todos os filmes disponiveis: ")
    response = requests.get(f"{API_URL}/filme")
    if response.status_code == 200:
        st.write("Deu certo")
        filmes = response.json().get("filmes", [])
    else:
        st.write("Não foi possivel exibir os filmes")