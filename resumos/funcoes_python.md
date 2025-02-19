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
### Argumentos nomeados
#### Argumentos nomeados de forma chave = valor

```
def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso! {marca}/{moddelo}/{ano}/{placa}")
```
#### Como passar os argumentos da função

```
salvar_carro(fiat, uno, 1999, ABC-1243)
salvar_carro(marca = "fiat", modelo = "uno", ano = "1999", placa = "ABC-1243")
salvar_carro(**{"marca": "fiat", "modelo" : "uno", "ano" : "1999", "placa" = "ABC-1243"})
```

### Utilizando tupla e dicionário

> Existem palavras por padrão que são utilizadas para indicar que o parâmetro que será recebido é uma tupla ou dicionário
>> - _*args_ o * indica que é uma tupla, podem ser utilizar outras palavras mas a args é mais utilizada
>> - _**kwargs_ os ** indicam que é um dicionário e assim como a anterior a palavra kwargs é mais utilizada

```
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args) #adicionando uma quebra de linha a cada parte da tupla, ou seja, valores separados por virgula
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()] # atribuindo um valor titulo a cada item do dicionário
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
exibir_poema("Sexta, 26 ago 22", "Zen of Python", "Beatiful is better than ugly.", author = "Tim peters", ano = 1999)
```


