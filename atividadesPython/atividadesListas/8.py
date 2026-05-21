# 8. Lista de compras

def inicio():
    compras = []

    while True:
        print("==== MENU COMPRAS ====")
        print("[1] Adicionar item")
        print("[2] Remover item")
        print("[3] Listar itens")
        print("[4] Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            item = input("Digite o item: ")
            compras.append(item)

        elif opcao == 2:
            item = input("Digite o item para remover: ")

            if item in compras:
                compras.remove(item)
                print("Item removido!")
            else:
                print("Item não encontrado!")

        elif opcao == 3:
            print("Lista de compras:")
            for item in compras:
                print(item)

        elif opcao == 4:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")

inicio()