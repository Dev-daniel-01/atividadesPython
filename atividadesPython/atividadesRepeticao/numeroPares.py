def inicio(): 
    numero = int(input("Digite um número: "))

    quantidade = 0

    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(i)
            quantidade += 1

    print("Quantidade de números pares:", quantidade)
inicio()