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
                    genero TEXT NOT NULL,
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

def cadastrar_filme(titulo, genero,  ano, nota):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
            "INSERT INTO filme (titulo, genero, ano, nota) "
            "VALUES (%s, %s, %s, %s)", (titulo, genero, ano, nota)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar filme: {erro}")
        finally:
            cursor.close()
            conexao.close()
cadastrar_filme("Interstellar", "Ficção Científica", 2014, 8.6)

def listar_filmes():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filme ORDER BY ID"
            )
            for linha in cursor.fetchall():
                print(linha)
        except Exception as erro:
            print(f"Erro ao listar filmes: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()
listar_filmes()