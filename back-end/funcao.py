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

def atualizar_nota(id, nova_nota):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filme SET nota = %s WHERE id = %s",
                (nova_nota, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar nota: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_filmes(id):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM filme WHERE id = %s",
                (id,)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Filme removido com sucesso!")
            else:
                print("Nenhum filme foi encontrado com o ID fornecido.")
        except Exception as erro:
            print(f"Erro ao tentar inserir filme:{erro}")
        finally:
            cursor.close()
            conexao.close()
deletar_filmes(8)
        

