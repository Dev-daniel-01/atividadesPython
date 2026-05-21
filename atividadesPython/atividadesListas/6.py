# 6. Lista B com dobro dos números da lista A

def inicio():
    listaA = []
    listaB = []

    for i in range(5):
        numero = int(input("Digite um número: "))
        listaA.append(numero)

    for numero in listaA:
        listaB.append(numero * 2)

    print("Lista A:", listaA)
    print("Lista B:", listaB)

inicio()