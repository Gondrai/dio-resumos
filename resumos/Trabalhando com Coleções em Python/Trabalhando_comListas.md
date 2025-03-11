# Listas 📖
### Podem armazenar de maneira sequencial qualquer tipo de objeto.
#### São objetos mutáveis
#### Para criar podemos utilizar:
  - list
  - função range
  - valores separados por virgulas dentro de colchetes

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


