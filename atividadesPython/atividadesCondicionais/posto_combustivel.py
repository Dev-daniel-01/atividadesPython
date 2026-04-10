def inicio():
    litros = float(input("Litros abastecidos: "))
    tipo = int(input("Tipo (1-Álcool / 2-Gasolina): "))
    preco = float(input("Preço por litro: "))

    if tipo == 1:
        desconto = 0.03 if litros <= 20 else 0.05
    elif tipo == 2:
        desconto = 0.04 if litros <= 20 else 0.06
    else:
        print("Tipo inválido")
        return

    total = litros * preco * (1 - desconto)
    print(f"Total a pagar: R$ {total:.2f}")

inicio()