while True:
    print ("====================")
    print (" Sistema de Cadastro")
    print ("====================")

    print ("1 - Cadastra")
    print ("2 - Fazer login")
    print ("3 - Sair " )

    opcao = int (input ("Escolha uma opção:"))
#Funcionalidades
    #se o usuario digitar o valor 1, vai ser exibido
    #a açao abaixo
    if(opcao == 1):
        print("======================")
        print("===tela de cadastro===")
        print("======================")
    elif(opcao == 2):
         print("=====================")
         print("====Tela de login====")
         print("=====================")
    else :
        print("Você esta saindo do cadastro, até mais")
        break 