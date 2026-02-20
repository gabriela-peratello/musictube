from database.conexao import conectar

def recuperar_generos():

    conexao, cursor = conectar()
    #Executando a consulta do gênero
    cursor.execute("SELECT generos_musicas, icone, cor FROM genero")

    #Recuperando os dados do gênero
    generos = cursor.fetchall()

    #Fechando a conexão
    conexao.close()

    return generos