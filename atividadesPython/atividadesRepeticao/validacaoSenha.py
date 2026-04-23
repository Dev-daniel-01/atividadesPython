def inicio():
    senha_correta = 2009
    tentativas = 0

    while True:
        senha = int(input("Digite a senha: "))
        tentativas += 1

        if senha == senha_correta:
            print(f"ACESSO PERMITIDO! Tentativas: {tentativas}")
            break
        else:
            print("ACESSO NEGADO!")

inicio()