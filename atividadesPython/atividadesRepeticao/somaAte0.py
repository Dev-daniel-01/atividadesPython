def inicio():
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        print("Nenhum número foi informado.")
    else:
        maior = numero
        menor = numero

        while True:
            numero = int(input("Digite um número (0 para parar): "))

            if numero == 0:
                break

            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero    
                
        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}")
inicio()