import mysql.connector

    #Transforma em estático
@staticmethod
def conectar():
    #Conectando no banco de dados
        conexao = mysql.connector.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "root",
            database = "onnemusic"
        )
        cursor = conexao.cursor(dictionary=True)

        return conexao, cursor