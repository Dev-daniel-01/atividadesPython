# 17. Simulação de lançamento de dado

import random

def inicio():
    resultados = []

    for i in range(20):
        numero = random.randint(1, 6)
        resultados.append(numero)

    print("Resultados:", resultados)

    for face in range(1, 7):
        quantidade = resultados.count(face)
        print(f"Face {face}: {quantidade} vezes")

inicio()