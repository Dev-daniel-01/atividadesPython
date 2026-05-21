# 8. Lista de compras usando match case

def inicio():
    compras = []

    while True:
        print("==== MENU COMPRAS ====")
        print("[1] Adicionar item")
        print("[2] Remover item")
        print("[3] Listar itens")
        print("[4] Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1:
                item = input("Digite o item: ")
                compras.append(item)
                print("Item adicionado!")

            case 2:
                item = input("Digite o item para remover: ")

                if item in compras:
                    compras.remove(item)
                    print("Item removido!")
                else:
                    print("Item não encontrado!")

            case 3:
                print("Lista de compras:")

                if len(compras) == 0:
                    print("Lista vazia!")
                else:
                    for item in compras:
                        print(f"\n{item}")

            case 4:
                print("Programa encerrado!")
                break

            case _:
                print("Opção inválida!")

inicio()