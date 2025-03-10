
MENU = f"""
|           MENU           |
|        1 - SAQUE         |
|        2 - DEPÓSITO      |
|        3 - EXTRATO       |
|        4 - SAIR          |
"""
# variaveis
saldo = 900
LIMITE_DE_SAQUES = 3
saque_dia = 0
VALOR_LIMITE = 500
extrato = f""" """

while True: 
    operacao = input(f"{MENU}")
    if operacao == "1" : 
        valor_saque = float(input("Qual valor deseja sacar?"))
        if valor_saque > saldo:
            print(f"Sua conta não possui esse valor, o saldo atual é de: {saldo:.2f}, favor selecionar valor válido")
        elif LIMITE_DE_SAQUES == saque_dia:
            print("Você já expirou a quantidade diária de saques, favor aguardar 24 horas para nova tentiva")
        elif valor_saque > VALOR_LIMITE: 
            print("O valor do saque é maior que o limite, favor selecionar valor até: R$ 500")
        else:
            extrato += f" Saque de R$: {valor_saque:.2f}\n"
            saldo -= valor_saque
            saque_dia += 1
            print(F"Realizado saque no valor de R$: {valor_saque:.2f}") 
    elif operacao == "2" :
        valor_deposito = float(input("Qual o valor do depósito?"))
        if valor_deposito > 0 :
            extrato += f" Depósito de R$: {valor_deposito:.2f}\n"
            saldo += valor_deposito
            print(f"Realizado depósito de R$: {valor_deposito:.2f}")
        else: 
            print("Não é possivel realizar o depósito, valor inválido")
    elif operacao == "3":
        print ("========= EXTRATO ========")
        if extrato == " ": 
            print("Não foram realizadas movimentações")
        else :
            print(f"{extrato}")
    elif operacao == "4":
        break
    

        



    
     

