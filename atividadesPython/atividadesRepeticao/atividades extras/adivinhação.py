import random
def inicio():

    numero = random.randint(1, 10)
    tentativas = 3

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Um jogo cheio de aventura e emoção (!)")
    print("Você tem 3 chances para acertar um número entre 1 e 10!\n")

    while tentativas > 0:

        palpite = int(input(f"Qual o seu palpite? (restam {tentativas} tentativas): "))

        if palpite < 1 or palpite > 10:
            print("\nDigite um número entre 1 e 10!\n")
        elif palpite == numero:
            print("\nVocê acertou! Parabéns!")
            break
        elif palpite < numero:
            print("\nMuito baixo!\n")
        else:
            print("\nMuito alto!\n")

        tentativas -= 1

    if palpite != numero and tentativas == 0:
        print(f"Não foi dessa vez! O número era {numero}.")

inicio()