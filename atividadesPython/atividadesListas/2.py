# 2. Ler 5 números, mostrar lista, soma e média

def inicio():
    numeros = []

    for i in range(5):
        numero = int(input("Digite um número: "))
        numeros.append(numero)

    soma = sum(numeros)
    media = soma / len(numeros)

    print(f"Números informados: {numeros}")
    print(f"Soma: {soma}")
    print(f"Média: {media}")

inicio()