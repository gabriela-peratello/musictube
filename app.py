from flask import Flask, redirect, render_template, request
import mysql.connector
from database.conexao import conectar
from model.genero import recuperar_generos
from model.musica import recuperar_musicas, salvar_musica


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

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    # Pegando os valores do formulário
    nome_musica = request.form.get("musicas")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    imagem = request.form.get("url_imagem")
    genero = request.form.get("genero")

    # Salvando a música no banco de dados
    if salvar_musica(cantor, nome_musica, duracao, imagem, genero):
        return redirect("/admin")
    else:
        return "Erro ao adicionar música"

if __name__ == "__main__":
    app.run(debug=True)