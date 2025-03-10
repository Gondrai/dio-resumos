## Interpolação de variáveis
### Em python existem 3 formas de interpolar variáveis: %, método format, f string. 
### A primeira forma não é recomendada, seu uso em python 3 é raro. Sendo f string a mais utilizada.
### %
nome = "Isabela"
idade = 76
profissao = "dev"
linguagem = "python"

print( "Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

###Método format

print( "Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}.".format(nome, idade, profissao, 
 linguagem))

### Também pode usar da forma, selecionando a posição das variáveis:

print( "Olá, me chamo {0}. Tenho {1} anos de idade, trabalho como {2} e estou matriculada no curso de {3}.".format(nome, idade, profissao, linguagem))

### f-string

print( f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.")
PI = 3.14159
print( f"Valor de PI: {PI:.2f}")
print( f"Valor de PI: {PI:10.2f}")


