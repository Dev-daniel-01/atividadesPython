def inicio():   
     velocidade_max = int(input("Digite a velocidade máxima da via: "))
     velocidade_motorista = int(input("Digite a velocidade do  motorista: "))
     if velocidade_motorista > velocidade_max:
        excesso = velocidade_motorista - velocidade_max
        multa = excesso * 5
        print(f"Multa: R$ {multa}")
     else:
        print("Não há multa.")

inicio()