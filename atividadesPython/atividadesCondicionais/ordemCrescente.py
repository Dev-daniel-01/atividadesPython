def inicio():
    num1 = int(input("informe o primeiro numero: "))
    num2 = int(input("informe o segundo numero: "))

    if num1 > num2:
        print(f"primeiro numero: {num1} é maior que {num2}")
    else:
        print(f"segundo numero: {num2} é maior que {num1}")

inicio()