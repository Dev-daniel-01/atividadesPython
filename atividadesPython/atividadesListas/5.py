# 5. Verificar se nome está na lista

def inicio():
    nomes = []

    for i in range(5):
        nome = input("Digite um nome: ")
        nomes.append(nome)

    busca = input("Digite um nome para buscar: ")

    if busca in nomes:
        print("O nome está presente na lista!")
    else:
        print("O nome não está presente na lista!")

inicio()