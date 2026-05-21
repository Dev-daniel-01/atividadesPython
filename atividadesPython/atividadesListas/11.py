# 11. Maior e menor valor com posições

def inicio():
    numeros = []

    for i in range(10):
        numero = int(input("Digite um número: "))
        numeros.append(numero)

    maior = max(numeros)
    menor = min(numeros)

    print(f"Maior valor: {maior}")
    print(f"Posição do maior: {numeros.index(maior)}")

    print(f"Menor valor: {menor}")
    print(f"Posição do menor: {numeros.index(menor)}")

inicio()