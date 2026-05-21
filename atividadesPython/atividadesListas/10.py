# 10. Mega-Sena

def inicio():
    gabarito = []
    aposta = []

    print("Digite os 6 números do gabarito:")

    for i in range(6):
        numero = int(input("Número: "))
        gabarito.append(numero)

    print("Digite os 10 números da aposta:")

    for i in range(10):
        numero = int(input("Número: "))
        aposta.append(numero)

    pontos = 0

    for numero in aposta:
        if numero in gabarito:
            pontos += 1

    print(f"O apostador fez {pontos} pontos.")

inicio()