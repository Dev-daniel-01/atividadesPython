def inicio():
    num = int(input("Digite um número: "))

    if num >= 0:
        if num % 2 == 0:
            print("Número positivo e par")
        else:
            print("Número positivo e ímpar")
    else:
        print(f"Valor absoluto: {abs(num)}")
# abs é valor absoluto
inicio()