# 12. Separar pares e ímpares

def inicio():
    numeros = []
    pares = []
    impares = []

    for i in range(15):
        numero = int(input("Digite um número: "))
        numeros.append(numero)

        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    print("Lista completa:", numeros)
    print("Pares:", pares)
    print("Ímpares:", impares)

inicio()