## Tipos de operadores em python 👩‍🔧 

  - Operadores aritméticos
  - Operadores de comparação
  - Operadores de atribuição
  - Operadores lógicos
  - Operadores de Identidade
  - Operadores de associação

### Operadores aritméticos ➕ 

 - +, -, *
 - /, // divisão inteira
 - % módulo
 - ** exponenciação

### Operadores de comparação 🟢🔴 

> Retorna false ou true:
- Menor igual (<=), Menor (<)
- Maior igual (>=), Maior (>)

### Operadores Lógicos 👨‍💻
- E (and)
```
Saldo >= saque and saque <= limite
```
- OU (or)
```
Saldo >= saque or saque <= limite
```
- Negação (not) 
```
not 1000> 1500
```
> [!Important]
> * Uma lista vazia no Python é considerado um valor boleano falso
> * Uma string vazia em python também tem valor boleano falso

### Operadores de identidade 🆔

> Compara se os objetos estão no mesmo lugar da memória
- is
- is not (para negação)
```
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200
curso is nome_curso
curso is not nome_curso
saldo is limite
```
### Operadores de associação 🔗

> Verifica se uma string está presente em outra
- in
- not in (para negação)
```
curso = "Curso de Python"
frutas = ["laranja", "uva". "limão
saques = [1500, 100]

"Python" in curso
"maça" not in frutas
```

