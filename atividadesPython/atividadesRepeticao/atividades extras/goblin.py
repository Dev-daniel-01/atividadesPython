import random
def inicio():

    numero = random.randint(1, 5)

    print("Bem-vindo à busca ao Goblin Irritado!")
    print("Um jogo cheio de aventura e emoção (!)\n")

    nome = input("Digite seu nome: ")

    print("\n|_1_| |_2_| |_3_| |_4_| |_5_|\n")

    while True:

        escolha = int(input("Em qual armário você acha que o goblin está [digite o número]: "))

        if escolha > 5 or escolha < 1:
            print("\nO número tem que ser de 1 até 5!\n")

        elif escolha != numero:
            print("\nDesculpe! O goblin ainda está à espreita em outro lugar!\n")

        else:
            print(f"\nBom trabalho {nome}! Você encontrou o goblin. Ele estava com tanto medo que fugiu!")
            break

inicio()