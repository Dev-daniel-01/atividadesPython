def inicio():   
    salario = float(input("Digite o seu salário: "))

    if salario < 0:
        print("Valor inválido")
    else:
        if salario < 1500:
            categoria = "Baixa renda"
            bonus = salario * 0.20
        elif salario <= 5000:
            categoria = "Classe média"
            bonus = salario * 0.10
        else:
            categoria = "Alta renda"
            bonus = salario * 0.05

        salario_final = salario + bonus

        print(f"Categoria: {categoria}")
        print(f"Salário com bônus: R$ {salario_final:.2f}")
inicio()