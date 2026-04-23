def inicio():
    numero = float(input("digite um numero: "))

    if numero >= 10:
        print("seu numero é maior que 10")
    elif numero < 10 and numero > 2:
        print("seu numero esta no intervalo de 2 a 10")
    else:
        print("seu numero é 1 ou 0")
inicio()