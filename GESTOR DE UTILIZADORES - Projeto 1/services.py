#Imports das funções de outros arquivos
from models import estrutura_utilizador #função da estrutura
from storage import carregar_dados,  guardar_dados #funções de guardar e carregar os dados do ficheiro json


#FUNÇÃO PARA GERAR OS ID 
def gerador_id (utilizadores): 
   
    utilizadores = carregar_dados ()
   
    if utilizadores:
    
         #para gerar novos id usamos condições o termo '[-1]' serve para começar a lista do fim, então ele contará do último id e adicionará mais um
         novo_id = utilizadores[-1]['id'] + 1
   
    else:
   
        #caso a lista esteja vazia, o id é 1
        novo_id = 1
   
    return novo_id
# FUNÇÃO PARA CRIAR NOVOS UTILIZADORES
def criar_utilizador (nome, email, idade):
  
    utilizadores = carregar_dados ()

# ESSAS CONDIÇÕES SÃO REGRAS DO SISTEMA
    # Se nome estiver em branco
   
    if nome == '':
        return False, 'Nome inválido!!!'
    # Se a idade for menor que 0 ou maior que 120
   
    elif idade <= 0 or idade >= 120:
        return False, 'Idade inválida!!!'
    # Para percorrer a lista de utilizadores para ver se o email já foi registrado
   
    for u in utilizadores:
        if u ['email'] == email:
            return False, 'email já registrado'
    # Senão irá ter um novo id e colocar todas as informações recebidas por parâmetro organizadas pela estrutura de utilizador
    else:
        novoid = gerador_id(utilizadores)

        novo_utilizador = estrutura_utilizador(novoid, email, nome, idade) #variavel que vai guardar as info

        utilizadores.append(novo_utilizador) #Adicionará o novo utilizador na lista de utilizadores dps de virar dicionario
        
        guardar_dados(utilizadores) # Por parâmetro irá enviar a variavel que guarda a lista de utilizadores para a função do storage 'guardar dados'
        
        return True, 'Novo utilizador criado com sucesso' # e retornar true com mensagem para o utilizador

#FUNÇÃO PARA APAGAR UTILIZADORES ATRAVÉS DE ID
def deletar_utilizador (apagar):
   
    utilizadores = carregar_dados ()
  
   # O For percorre a lista utilizadores com o if o id na variavel apagar recebido pelo parâmetro será comparado com os id da lista e serã removida
    for u in utilizadores:
    
        if u ['id'] == apagar:

            #função para remover o utilizador que estã guardado na váriavel 'u'
            utilizadores.remove(u)
            
            guardar_dados(utilizadores) #guardar a nova lista
            
            return True, 'Utilizador Removido com Sucesso' # mensagem do sucesso
    
        else:
            return False, 'ID não encontrado'
        
def listagem_utilizadores ():
    return carregar_dados ()