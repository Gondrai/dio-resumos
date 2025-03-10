# Estruturas condicionais ⚖ 
### Em python existem alguns tipo de estruturas condicionais:
#### - if
Válida se determinado valor segue o parametro indicado na estrutura e executa uma série de códigos do bloco, caso corresponda.
```
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizado saque!")

if saldo < saque: 
    print("O valor do saque é maior que o saldo em conta, favor selecionar valor válido")
```
#### - if/else
Faz o mesmo que o anterior, mas caso não corresponde ele executa outro bloco (else) determinado.

```
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizado saque!")
else:  
    print("O valor do saque é maior que o saldo em conta, favor selecionar valor válido"
```
#### if/elif/else
Faz o mesmo que o anterior, porém ele permite que mais de uma condição seja questionada. 

```
opcao = int(input("Informe uma opção: [1] Sacar\n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    #
elif opcao == 2;
    print ("Exibindo extrato....")
else: 
    sys.exit("Opção inválida")
```
#### if aninhado

Basta adicionar estruturas if/elif/else dentro de outras estrutruturas if/elif/else.

```

```
