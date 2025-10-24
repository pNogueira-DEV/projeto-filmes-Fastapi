from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS filmes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    diretor TEXT NOT NULL,
                    ano INT NOT NULL,
                    nota FLOAT
                    )
                """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()


