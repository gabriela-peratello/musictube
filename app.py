from flask import Flask, render_template
import mysql.connector
from database.conexao import conectar
from model.genero import recuperar_generos
from model.musica import recuperar_musicas


app = Flask(__name__)


#Abre a página principal, GET = pega e envia para o usuário
@app.route("/home", methods=["GET"])
#Não precisa por get pq ele é padrão
@app.route("/")                   
def pagina_principal():
    # Recuperando as músicas
    musicas = recuperar_musicas()
    # Recuperando os gêneros
    generos = recuperar_generos()

    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def pagina_admin():
    # Recuperando as músicas 
    musicas = recuperar_musicas()
    # Recuperando os gêneros
    generos = recuperar_generos()
    # Mostrando a página
    return render_template("administracao.html", musicas = musicas, generos = generos)

if __name__ == "__main__":
    app.run(debug=True)