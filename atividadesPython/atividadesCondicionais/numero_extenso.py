def inicio():
    num = int(input("Digite um número de 0 a 9: "))

    numeros = [
        "Zero", "Um", "Dois", "Três", "Quatro",
        "Cinco", "Seis", "Sete", "Oito", "Nove"
    ]

    if 0 <= num <= 9:
        print(numeros[num])
    else:
        print("Valor inválido")

inicio()