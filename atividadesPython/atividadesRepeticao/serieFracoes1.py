def inicio():
    soma = 0

    for i in range(1, 101):
        soma += i / (101 - i)

    print(f"Resultado: {soma:.2f}")

inicio()