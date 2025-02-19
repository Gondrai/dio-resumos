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
### Parâmetros Especiais
#### Esses parâmetros têm a definição se devem ser só por posição ou nomeados também. 

> Sintaxe
>> ``` def f (pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):```
>> - / - até onde ficam os posicionais apenas
>> - _*_ Até onde podem ser nomeados ou posicionais também
>> - Após o _*_ todos os que são somente nomeados

## Objetos de primeira classe
### Em python _tudo_ é objeto, inclusive funções
#### Sendo assim, podemos atribuir funções a variáveis, passar elas como parâmetro para funções, usá-las como valores em estruturas de dados. 
 
```
def somar(a,b):
    return a+b

def exibir_resultado(a,b, funcao):
    resultado = funcao(a,b)
    print(f"o resultado da operacao {a} + {b} = {resultado}")

exibir_resultado(10,10, somar)
```

## Escopo local e global 
### Dentro de um bloco de função o escopo é local
#### - A palavra-chave **_global_**, informa ao interpretador que a variável utilizada no escopo local é global.
> [!CAUTION]
> Não é uma boa prática e deve ser evitada. 

```
salario = 2000

def salario_bonus(bonus):
    global salario # informando que a variavel é global
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)

```

