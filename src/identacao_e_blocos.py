
def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print ("Valor sacado!")
        print("Tire o dinheiro na boca do caixa.")


def depositar(valor):
    saldo = saldo+valor
    print("Seu saldo é: ", saldo)

sacar(100)
depositar(900)



