def inicio():
    num = int(input("Digite um número: "))

    if num % 2 == 0 or num % 7 == 0:
        print("Divisível por 2 ou por 7")
    else:
        print("Não é divisível por 2 nem por 7")

inicio()