def inicio():
    copias = int(input("Quantidade de cópias: "))

    if copias <= 100:
        total = copias * 0.25
    else:
        total = (100 * 0.25) + ((copias - 100) * 0.20)

    print(f"Total a pagar: R$ {total:.2f}")

inicio()