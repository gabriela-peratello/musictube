from database.conexao import conectar

def cadastrar(usuario, senha):
    conexao, cursor = conectar()
    try:
        # Executar o INSERT
        cursor.execute("""
                    INSERT INTO cadastro
                    (usuario, senha)
                    VALUES(%s, %s)
        """,
        [usuario, senha])

        conexao.commit()
        conexao.close()
        return True
    except:
        return False



