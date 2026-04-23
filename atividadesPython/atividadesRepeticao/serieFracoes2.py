def inicio():
    soma = 0
    numerador = 1
    denominador = 1

    for i in range(20):
        soma += numerador / denominador
        numerador += 2
        denominador *= 2

    print(f"Resultado: {soma:.2f}")

inicio()