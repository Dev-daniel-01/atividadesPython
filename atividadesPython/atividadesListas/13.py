# 13. Lista invertida sem reverse()

def inicio():
    numeros = []

    for i in range(10):
        numero = int(input("Digite um número: "))
        numeros.append(numero)

    print("Lista invertida:")

    for i in range(len(numeros) - 1, -1, -1):
        print(numeros[i])

inicio()