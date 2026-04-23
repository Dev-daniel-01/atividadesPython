def inicio():
    numero = int(input("Digite um número: "))
    inicio_intervalo = int(input("Começar por: "))
    fim = int(input("Terminar em: "))

    for i in range(inicio_intervalo, fim + 1):
        print(f"{numero} x {i} = {numero * i}")

inicio()