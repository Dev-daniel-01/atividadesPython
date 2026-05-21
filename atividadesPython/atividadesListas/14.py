# 14. Intercalar duas listas

def inicio():
    listaA = []
    listaB = []
    listaC = []

    print("Digite os valores da lista A:")

    for i in range(5):
        numero = int(input("Número: "))
        listaA.append(numero)

    print("Digite os valores da lista B:")

    for i in range(5):
        numero = int(input("Número: "))
        listaB.append(numero)

    for i in range(5):
        listaC.append(listaA[i])
        listaC.append(listaB[i])

    print("Lista intercalada:", listaC)

inicio()