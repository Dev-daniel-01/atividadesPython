def inicio():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")

    match op:
        case '+':
            print("Resultado:", a + b)
        case '-':
            print("Resultado:", a - b)
        case '*':
            print("Resultado:", a * b)
        case '/':
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Erro: divisão por zero")
        case _:
            print("Operação inválida")

inicio()