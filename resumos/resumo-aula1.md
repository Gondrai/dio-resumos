# Resumo de alterações

## 📁 Ignorar Pasta
### Se add o cód:
```
echo resumos/ > .gitignore
```
|💡 Termo| Significado|
|--------|------------|
|echo| escreva|
|resumos| pasta que deseja que o git ignore|
|.gitignore| texto indicando que a pasta deve ser ignorada|

## 🗂 Reconhecimento de diretório

### O git não reconhece repositórios vazios com o comando git status, para isso foi criada a convenção de cód
```
touch aulas/.gitkeep
```
|💡 Termo| Significado|
|--------|------------|
|touch| cria arquivo|
|aulas| pasta que será criado o arquivo|
|.gitkeep|arquivo que indica que a pasta deve ser identificada|

## 👆🏽 Coisas importantes
```
git mkdir # criar diretório
```
```
git log # trazer o log de commits
```
```
git log # trazer o log de commits, mais detalhado
```
```
git restore # trazer o log de commits (descarta todas as alterações localmente)
```
```
rm -rf .git # remover diretório de maneira recursiva
```
```
cat config # exibir conteúdo de um arquivo
```
```
git clone endereco_url nome-da-pasta-pc # exibir conteúdo de um arquivo
```
```
git remote - v # verificar repositórios remotos
```
```
git remote add origin url_repositorio # add repositórios remotos
```
```
git push -u origin main # "Empurrar" as modificações para o repositório remoto
```
```
git remote add origin url_repositório #conectar com repositório remoto
```
```
git commit --amend -m "add" #renomear o commit
```
```
git reset --soft #retorna para o commit anterior
```
```
git reset --mixed #comportamento padrão, move os arquivos do ultimo commit para o untracked file
```
```
git reset --hard _commit_que deseja_retornar #apaga os arquivos dos commits
```
```
git checkout -b nome_branch #cria nova branch
```
```
git checkout nome_branch #se locomover entre as branchs
```
```
git branch -v #mostra as brachs
```
```
git merge nome_branch #merge duas branchs
```
```
git branch -d nome_branch #deletar branch
```
[Markdown basics](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)