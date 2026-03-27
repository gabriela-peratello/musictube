import mysql.connector

    #Transforma em estático

status ="NUVEM"

@staticmethod
def conectar():
        if status == "LOCAL":
    #Conectando no banco de dados
            conexao = mysql.connector.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "root",
            database = "onnemusic"
        )
        else:
            conexao = mysql.connector.connect(
            host = 'servidor-peratello-servidor-peratello.a.aivencloud.com',
            port = 18747,
            user = 'avnadmin',
            password = 'AVNS_8H7HnrF8LpNDo2p6Q8A',
            database = "onnemusic"
        )



        cursor = conexao.cursor(dictionary=True)

        return conexao, cursor