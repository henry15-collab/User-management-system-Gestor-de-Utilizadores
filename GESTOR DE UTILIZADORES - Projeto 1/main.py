

import os
from services import criar_utilizador, deletar_utilizador, listagem_utilizadores

def escolha_de_opcao ():
   
    escolha = int (input ('Insira a sua opção: '))

    if escolha == 1:
      
        os.system ('cls')
      
        nome = input ('Insira seu nome: ')
        email = input ('Insira seu email: ')
        idade = int ((input ('Insira sua idade: ')))
            
        sucesso, resultado = criar_utilizador (nome, email, idade)
        print (resultado, f'\n')
        input (('pressione ENTER para continuar..'))
      
        os.system ('cls')
   
    elif escolha == 2:
       
        utilizadores = listagem_utilizadores()
      
        if not utilizadores:
            os.system ('cls')
       
            print("Nenhum utilizador registado.\n")
            input (('pressione ENTER para continuar..'))
      
            os.system ('cls')
      
        else:
          
            os.system ('cls')
          
            for u in utilizadores:
           
                print(f"ID: {u['id']}")
          
                print(f"Nome: {u['nome']}")
          
                print(f"Email: {u['email']}")
          
                print(f"Idade: {u['idade']}")
            
                print("-" * 40)
                input (('pressione ENTER para continuar..'))
          
                os.system ('cls')
  
    elif escolha == 3:
       
        os.system ('cls')
       
        apagar = int (input ('Insira o ID do utilizador que você deseja deletar: '))
        sucesso, msg = deletar_utilizador (apagar)
       
        print(msg, f'\n')
        input (('pressione ENTER para continuar..'))
       
        os.system ('cls')
    
    else:
        pass
    return escolha

def start ():
   
    os.system ('cls')
    opcao = 1
   
    while opcao != 4:
        print ('-'*50)
        print ('Gestor de Utilizadores')
        print ('-'*50)
        print ('1. Criar Utilizador')
        print ('2. Listar Utilizadores já criados')
        print ('3. Remover Utilizador')
        print ('4. Sair')
      
        opcao = escolha_de_opcao ()






if __name__ == '__main__':
    start ()