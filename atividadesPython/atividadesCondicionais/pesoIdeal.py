def inicio():
    altura = float(input("Digite sua altura (ex: 1.75): "))
    genero = input("Digite seu gênero (M/F): ").strip().lower()

    if genero in ['m', 'masculino']:
        peso_ideal = 72.7 * altura - 58
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

    elif genero in ['f', 'feminino']:
        peso_ideal = 62.1 * altura - 44.7
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

    else:
        print("Gênero inválido! Use M ou F.")

inicio()