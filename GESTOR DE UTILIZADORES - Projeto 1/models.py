#função para criar organizar a informação dos utilizadores no ficheiro json.
def estrutura_utilizador(id,email,nome,idade):#o parâmetro recebe esses 4 argumentos enviados pelo Services
    utilizador = {
        'id': id,
        'email': email,
        'nome': nome,
        'idade': idade

    }
    return utilizador #retorna com uma váriavel do tipo dicionário que contém a organização