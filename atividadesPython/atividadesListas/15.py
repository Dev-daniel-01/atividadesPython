# 15. Simulação de fila

def inicio():
    fila = []

    while True:
        print("==== FILA ====")
        print("[1] Entrar na fila")
        print("[2] Chamar próximo")
        print("[3] Mostrar fila")
        print("[4] Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Nome da pessoa: ")
            fila.append(nome)

        elif opcao == 2:
            if len(fila) > 0:
                print(f"{fila.pop(0)} foi chamado.")
            else:
                print("Fila vazia!")

        elif opcao == 3:
            print("Fila atual:", fila)

        elif opcao == 4:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")

inicio()