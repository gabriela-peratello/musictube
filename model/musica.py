from database.conexao import conectar



def recuperar_musicas():
    # Passo 1 e 2 realizados
    conexao, cursor = conectar()

    #Executando a consulta
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_capa, genero FROM musica;")
    #Recuperando os dados e guardando
    musicas = cursor.fetchall()

    #Fechar conexão
    conexao.close()

    return musicas

def salvar_musica(cantor:str, nome_musica:str, duracao:str, url_imagem:str, genero:str) -> bool:
    """ Essa função tem como intuito de adicionar uma música."""

    try:
        conexao, cursor = conectar()
        # Executar o insert
        cursor.execute("""
                    INSERT INTO musica (cantor, nome, duracao, url_capa, genero) 
                    VALUES (%s, %s, %s, %s, %s);
                    """,
                    (cantor, nome_musica, duracao, url_imagem, genero )
                    )
        # Confirmando o insert
        conexao.commit()
        conexao.close()

        return True
    except:
        return False