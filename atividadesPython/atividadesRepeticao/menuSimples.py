def inicio():
    while True:
        print("\n# MENU PRINCIPAL #")
        print("[1] Inserir")
        print("[2] Editar")
        print("[3] Excluir")
        print("[4] Listar")
        print("[5] Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("Você escolheu Inserir!")
        elif opcao == 2:
            print("Você escolheu Editar!")
        elif opcao == 3:
            print("Você escolheu Excluir!")
        elif opcao == 4:
            print("Você escolheu Listar!")
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

inicio()