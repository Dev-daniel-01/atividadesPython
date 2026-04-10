def inicio():
    num = int(input("Digite um número: "))

    if num % 2 == 0 and num % 3 == 0:
        print("Divisível por 2 e por 3")
    else:
        print("Não é divisível por ambos")

inicio()