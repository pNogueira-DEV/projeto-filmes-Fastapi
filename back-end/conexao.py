import mysql.connector #conectar com o banco de dados
from dotenv import load_dotenv #pegar valores do .env(uma criptografia simples)
import os #trabalhar com variaveis de ambiente do sistema operacional#Carregar .env


#carregar .env
load_dotenv()


def conector():
    try:
        conexao = mysql.connector.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        cursor = conexao.cursor()
        print("Conexão bem sucedida!")
        return conexao, cursor
    except mysql.connector.Error as error:
        print(f"Erro de conexão: {error}")
        return None, None 