# 3. Lista de 1 a 20 mostrando apenas pares

def inicio():
    numeros = []

    for i in range(1, 21):
        numeros.append(i)

    print("Números pares:")

    for numero in numeros:
        if numero % 2 == 0:
            print(numero)

inicio()