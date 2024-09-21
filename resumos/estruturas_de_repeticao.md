# Estruturas de repetição
#### Estrututas utilizadas para repetir um trecho de código.
#### - For:
Ideal para quando sabemos o número de iterações necessárias.

```
texto = input("Infome um texto: ")
VOGAIS = "AEIOU"
for letra in texto: 
    if letra.upper() in VOGAIS
        print(letra, end = "")
print( ) #adiciona uma quebra de linha

```

#### - Range :
Recebe 3 argumentos
 - Stop (Obrigatório)
 - Start (Opcional)
 - Step (Opcional)
```
# range(stop) -> range object
# range(start, stop[step] -> range object
---------------------------------------------------
list(range(4))
>>> [0,1,2,3]
```
Exemplo de uso dos 3 argumentos 
```
# tabuada do 5
for numero in range(1, 50, 5):
    print(numero, end="")
```
#### - While
Ideal para quando não sabemos previamente o número de iterações necessárias.

```
while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Fazer depósito \n [0] Sair))

    if opcao = 1

```
