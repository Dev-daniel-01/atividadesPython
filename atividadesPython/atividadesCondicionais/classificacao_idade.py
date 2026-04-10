def inicio():
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Menor de idade")
    elif idade >= 65:
        print("Terceira idade")
    else:
        print("Maior de idade")

inicio()