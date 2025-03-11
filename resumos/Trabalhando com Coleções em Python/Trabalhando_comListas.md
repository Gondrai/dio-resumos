# Listas 📖
### Podem armazenar de maneira sequencial qualquer tipo de objeto.
#### São objetos mutáveis
#### Para criar podemos utilizar:
  - list;
  - função range;
  - valores separados por virgulas dentro de colchetes.

```
frutas = ["laranja", "maca", "uva"]
frutas= []
letras = list("python") - cada letra é um  (a string é um elemento iterável)
numeros = list(range(10))
carro  = ["Ferrari, "F8", 4200000, 2020, 2900, "São Paulo", True]

```
## Formas de acessar a lista

### Acesso direto
#### A lista é uma sequência, podemos acessar os dados utilizando índices. 

```
frutas = ["laranja", "maca", "uva"]
frutas[0] # Maçã
frutas[2] # Uva

```
#### Em python também podemos utilizar índices negativos

```
frutas = ["laranja", "maca", "uva"]
frutas[-1] # Uva
frutas[-3] # 

```

### Listas aninhadas
#### No python, listas também são objetos, assim podemos criar listas que guardam outras listas. Podemos criar estruturas bidimensionais (tabelas), e acessar informando índice de linha e coluna.

 - Podemos utilizar para representar matrizes 

```
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

```

### Fatiamento
#### Podemos extrair um conjunto de valores de uma sequência, para isso basta passar o índice inicial e/ou final para acessar o conjunto. Ainda podemos pular posições.

```
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[0:3:2] # ["p", "t" ]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

# É obrigatório indicar o índice inicial ou final, não precisa passar os dois
# obs: existe 1 excessão lista[::], serve para criar cópia de lista, colocando tudo vazio

```
### Iterar listas

### For
#### A forma mais comum de percorrer listas é utilizando o comando for.

```
carro = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

```
### Enumerate 

```
carro = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

```

## Compressão de listas

### Oferece uma sintaxe mais curta quando queremos:
    - Criar uma nova lista com base nos valores de um filtro;
    - Gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

```
# filtro versão 1
# Pegando todos os valores pares de uma lista existente

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

```

```
# filtro versão 2
# Pegando todos os valores pares de uma lista existente

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

```

```
# versão 1
# Modificando valores

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

```

```
# versão 2
# Modificando valores

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]


```








