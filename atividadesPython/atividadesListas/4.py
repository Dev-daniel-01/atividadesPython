# 4. Mostrar lista ao contrário

def inicio():
    numeros = []

    for i in range(5):
        numero = int(input("Digite um número: "))
        numeros.append(numero)

    print("Lista original:", numeros)

    numeros.reverse()

    print("Lista ao contrário:", numeros)

inicio()