## Funções
### Um bloco de código identificado por um nome, pode receber uma lista de parêmetros.
####  - Entradas: parâmetros
####  - Saídas: retornos

> Palavra reservada para definição de funções
>> - _def_ Informa ao interpretador o nome de uma função

```
def exibir_mensagem():
    print("Olá mundo")
```
#### Recebendo atributos

```
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem_2( nome = "Guilherme")
```

### Retorno de valores 

> Palavra reservada para retorno de funções
>> - _return_
>> - Toda função em python retorna **_None_** por padrão

```
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

calcular_total([10,40,60])
retorna_antecessor_e_sucessor(10)

```




