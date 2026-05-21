# 9. Lista sem números repetidos

def inicio():
    numeros = []

    while len(numeros) < 5:
        numero = int(input("Digite um número: "))

        if numero not in numeros:
            numeros.append(numero)
        else:
            print("Número repetido! Digite outro.")

    print("Lista final:", numeros)

inicio()