def inicio():
    while True:
        print("\n# MENU PRINCIPAL #")
        print("[1] Inserir")
        print("[2] Editar")
        print("[3] Excluir")
        print("[4] Listar")
        print("[5] Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                print("Você escolheu Inserir!")
            case 2:
                print("Você escolheu Editar!")
            case 3:
                print("Você escolheu Excluir!")
            case 4:
                print("Você escolheu Listar!")
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")

inicio()