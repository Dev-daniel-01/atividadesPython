# 10. Mega-Sena

def inicio():
    gabarito = [5, 12, 23, 34, 45, 60]
    aposta = []

    print("Digite os 10 números da aposta:")

    for i in range(10):
        numero = int(input("Número: "))
        aposta.append(numero)

    pontos = 0

    for numero in aposta:
        if numero in gabarito:
            pontos += 1

    print("Gabarito:", gabarito)
    print("Aposta:", aposta)
    print(f"O apostador fez {pontos} pontos.")

inicio()