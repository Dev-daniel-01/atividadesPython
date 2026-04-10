def inicio():
    numero = int(input("digite um numero: "))

    if numero < 0:
        absoluto = -numero
    else:
        absoluto = numero
        
    print(f"seu numero é: {numero} e o valor absoluto dele é {absoluto}")
inicio()