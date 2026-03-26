from database.conexao import conectar

# Verifica se há cadastro e se tiver, retorna os dados do usuário selecionado

def verificar_usuario(usuario:str, senha:str):
    conexao, cursor = conectar()
    cursor.execute("""
                   SELECT usuario, senha FROM cadastro 
                    WHERE usuario = %s AND senha = %s
                   """, [usuario, senha]) 
    usuario = cursor.fetchone()
    
    conexao.close()
    return usuario 

