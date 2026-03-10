import json
# Storage com a função de ler e guardar o arquivo json


dados = 'dados.json' #o arquivo json guardado como variavel e str

#Função para guardar os dados
def guardar_dados (utilizadores):
    
    #'With' garante que o ficheiro irar fechar automaticamente
    
    #'Open' abre o ficheiro guardado em 'dados'
    
    #a str 'w' tem a função de write cria o ficheiro se não existir apaga tudo e escreve de novo
    
    # 'ficheiro' é o nome da variavel do ficheiro aberto
    with open (dados, 'w') as ficheiro:

        #Função que escreve dados no ficheiro
        json.dump (utilizadores, ficheiro, indent=4)
            # O dado que será salvo, Onde será escrito (ficheiro aberto), Organiza o JSON com identação
def carregar_dados ():
   
    try: #Tenta executar um bloco - Se der erro → pula para except
        
        # 'r' Modo read (leitura)

        with open(dados, "r") as ficheiro:

            #'json.load' Converte JSON → Python
            return json.load(ficheiro)
        
     #Esse erro acontece quando: o ficheiro ainda não existe ao invés de quebrar o programa e retornar nada e segue.
    except FileNotFoundError:
        return []