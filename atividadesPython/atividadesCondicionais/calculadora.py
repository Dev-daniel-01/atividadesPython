def inicio():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")

    if op == '+':
        print("Resultado:", a + b)
    elif op == '-':
        print("Resultado:", a - b)
    elif op == '*':
        print("Resultado:", a * b)
    elif op == '/':
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Erro: divisão por zero")
    else:
        print("Operação inválida")

inicio()