## Classe String Python 
### Manipular sequências de caracteres.
### Métodos úteis da classe string
curso = "  Curso de Python  "
### upper()
### Converte todos os carcteres para maisculo
print(curso.upper())
### lower()
### Converte todos os carcteres para maisculo
print(curso.lower())
### title()
### Converte todos os carcteres para minusculo, exceto o primeiro
print(curso.title())
### strip()
### Remove os espaços em branco da direita e esquerda
print(curso.strip())
### lstrip()
### Remove os espaços em branco da esquerda
print(curso.lstrip())
### rstrip()
### Remove os espaços em branco da direita
print(curso.rstrip())
### center()
### Centraliza o objeto, pode receber dois parametros, a quantidade de caracteres que a palavra terá e qual o caractere será inserido para preencher esse valor.
print(curso.center(25, "#"))
### join(string)
### Serve para juntar carcteres a nossa string, serve para todo tipo iterável, ele vai iterar a cada item. (Mais comum utilizar em listas)
print ( ".".join(curso))