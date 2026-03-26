from flask import Flask, flash, redirect, render_template, request, session
import mysql.connector
from database.conexao import conectar
from model.genero import recuperar_generos
from model.musica import apagar_musica, recuperar_musicas, salvar_musica, status_musica
from model.usuario import cadastrar
from model.usuario_model import verificar_usuario


app = Flask(__name__)

app.secret_key = "senhaMuitoBemPensada"


#Abre a página principal, GET = pega e envia para o usuário
@app.route("/home", methods=["GET"])
#Não precisa por get pq ele é padrão
@app.route("/")                   
def pagina_principal():
    # Recuperando as músicas
    musicas = recuperar_musicas(True)
    # Recuperando os gêneros
    generos = recuperar_generos()

    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def pagina_admin():
    if "usuario-logado" not in session:
        return redirect ("/login")
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
    

@app.route("/musica/excluir/<codigo>")
def deletar_musica (codigo):
    apagar_musica (codigo)
    return redirect("/admin") 

@app.route("/musica/ativar/<ativar>/<codigo>")
def ativar_musica(ativar, codigo):
    status_musica(ativar, codigo)
    return redirect("/admin")

@app.route("/cadastro")
def pag():
    return render_template("cadastro.html")


@app.route("/cadastro/post", methods=["POST"])
def por_cadastrar():
   usuario = request.form.get("usuario")
   senha = request.form.get("senha")

   if cadastrar(usuario, senha):
       return redirect("/admin")
   else:
       return "<h1> Erro ao cadastrar. Tente novamente. </h1>"
   
@app.route("/login", methods = ["GET", "POST"])
def logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    usuario = verificar_usuario(usuario, senha)

    if usuario:
        session["usuario_logado"] = usuario
        flash(f"Seja bem-vindo, {usuario.nome}")
        return redirect ("/admin")
    else:
        flash("Usuário ou senha iválidos.", "danger")
        return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)



    