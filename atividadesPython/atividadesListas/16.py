# 16. Temperaturas de 10 dias

def inicio():
    temperaturas = []

    for i in range(10):
        temperatura = float(input("Digite a temperatura: "))
        temperaturas.append(temperatura)

    media = sum(temperaturas) / len(temperaturas)
    maior = max(temperaturas)
    menor = min(temperaturas)

    acima_media = 0

    for temperatura in temperaturas:
        if temperatura > media:
            acima_media += 1

    print(f"Média: {media}")
    print(f"Maior temperatura: {maior}")
    print(f"Menor temperatura: {menor}")
    print(f"Dias acima da média: {acima_media}")

inicio()