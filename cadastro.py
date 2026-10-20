#variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""
#variaveis de login 
usuario = ""
senha = ""
while True:
    print ("====================")
    print (" Sistema de Cadastro")
    print ("====================")

    print ("1 - Cadastra")
    print ("2 - Fazer login")
    print ("3 - Sair " )

    opcao = input("Escolha:")
    #Funcionalidades
    #se o usuario digitar o valor 1, vai ser exibido
    #a açao abaixo
    if (opcao == "1"):
        print("======================")
        print("===tela de cadastro===")
        print("======================")
        nome = input("digite o seu nome: ")
        idade = input("digite o sua idade: ")
        usuario = input("digite o seu usuario: ")
        senha = input("digite o sua senha: ")
        print("\n cadastro realizado!\n")
        #se digitar 2, abre a tela de login
    elif (opcao == "2"):
         print("=====================")
         print("====Tela de login====")
         print("=====================")
         #se digitar 3,para a executado"
         login_usuario = input("digite o usuario: ")
         login_senha = input("digite a sua senha: ")

         #processamento de usuario e senha
    if login_usuario == usuario and login_senha == senha  :
         print("\n login realizado com sucesso!\n ")
         print("bem vindo, nome")
     #Se não estiver correto entra no caso abaixo
     else:
         print ("Usuário ou senha incorretos ")   
  #se digitar 3, sai da execução  
    elif(opcao == "3"):
         print("Você esta saindo do cadastro, até mais")
         break 

    