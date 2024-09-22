## Classe String Python 
### Manipular sequências de caracteres.
#### Métodos úteis da classe string: 
- upper()
  
  > Converte todos os carcteres para maisculo
  ```
  print(curso.upper())
  ```
- lower()
  
  > Converte todos os carcteres para maisculo
   ```
  print(curso.lower())
  ```
- title()
  
  > Converte todos os carcteres para minusculo, exceto o primeiro
   ```
  print(curso.title())
  ```
- strip()
  
  > Remove os espaços em branco da direita e esquerda
   ```
  print(curso.strip())
  ```
- lstrip()
  
  > Remove os espaços em branco da esquerda
   ```
  print(curso.lstrip())
  ```
- rstrip()
  
  > Remove os espaços em branco da direita
   ```
  print(curso.rstrip())
  ```
- center()
  
  > Centraliza o objeto, pode receber dois parametros, a quantidade de caracteres que a palavra terá e qual o caractere será inserido para preencher esse valor.
  ```
  print(curso.center(10, "#")
  ```
- join(string)
  
  > Serve para juntar carcteres a nossa string, serve para todo tipo       iterável, ele vai iterar a cada item. (Mais comum utilizar em listas)
    ```
    print ( ".".join(curso))
    ```

## Interpolação de variáveis
### Em python existem 3 formas de interpolar variáveis: %, método format, f string. 
> [!warning]
> A primeira forma não é recomendada, seu uso em python 3 é raro. Sendo f string a mais utilizada.
  - %
    
    ```
    nome = Isabela
    idade = 76
    profissao = dev
    linguagem = python

    print( "Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." (nome, idade, profissao,   
     linguagem))
    ```
  -  Método format
      ```
      nome = Isabela
      idade = 76
      profissao = dev
      linguagem = python

      print( "Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}.".format (nome, idade, profissao,   
     linguagem))

      ### Também pode usar da forma, selecionando a posição das variáveis:

      print( "Olá, me chamo {1}. Tenho {2} anos de idade, trabalho como {3} e estou matriculada no curso de {4}.".format (nome, idade, profissao, linguagem))
      
      ```
      
  - f-string
    ```
    nome = Isabela
    idade = 76
    profissao = dev
    linguagem = python

    print( "Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.")
    ```
