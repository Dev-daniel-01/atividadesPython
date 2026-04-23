def inicio():
    soma = 0

    while True:
        numero = int(input("Digite um número (0 para parar): "))
        soma += numero
        if numero == 0:
            break
        
    print("Soma total:", soma)
inicio()